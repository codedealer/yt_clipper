#!/usr/bin/env python3

import os
import sys
from pathlib import Path

import certifi

from clipper import (
    argparser,
    clip_maker,
    clipper_types,
    util,
    ytc_logger,
    ytc_settings,
)
from clipper.clipper_types import ClipperState
from clipper.ffmpeg_version import getFfmpegVersion
from clipper.version import __version__
from clipper.ytc_logger import logger
from clipper.ytdl import ytdl_bin_get_version

UNKNOWN_PROPERTY = "unknown"


def main() -> None:
    cs = clipper_types.ClipperState()

    args, unknown, argsFromArgFiles, argFiles, argsFromArgFilesMap = argparser.getArgs()

    cs.settings.update({"color_space": None, **args})
    ytc_settings.loadSettings(cs.settings)

    setupDepPaths(cs)

    if cs.settings["printVersions"]:
        print(argparser.getDepVersionsString(cs.clipper_paths))
        sys.exit(0)

    setupOutputPaths(cs)

    ytc_logger.setUpLogger(cs)

    logger.debug(f"yt-dlp path set: {cs.clipper_paths.ytdlPath}")

    logger.report(f"yt_clipper version: {__version__}")
    logger.report(
        f"yt-dlp version: {ytdl_bin_get_version(cs.clipper_paths)}",
    )
    logger.report(f"{getFfmpegVersion(cs.clipper_paths.ffmpegPath)}", extra={"highlighter": None})
    logger.info("-" * 80)

    logger.debug(f"The following  arguments were read from the command line {sys.argv[1:]}:")

    if argsFromArgFiles:
        logger.notice(f"The following default arguments were read from {argFiles}:")
        logger.notice(argsFromArgFilesMap)
        logger.info("-" * 80)
    elif argFiles:
        logger.notice(f"No uncommented arguments were found in {argFiles}")
        logger.info("-" * 80)

    if unknown:
        logger.notice(
            f"The following unknown arguments were provided and were ignored:",
        )
        logger.notice(unknown)
        logger.info("-" * 80)

    ytc_settings.getInputVideo(cs)

    ytc_settings.getGlobalSettings(cs)

    logger.info("-" * 80)
    if not cs.settings["preview"]:
        clip_maker.makeClips(cs)
    else:
        clip_maker.previewClips(cs)

    ytc_logger.printReport(cs)

    if cs.settings["notifyOnCompletion"]:
        util.notifyOnComplete(cs.settings["titleSuffix"])

def prepareTopazFFmpeg(cs: ClipperState) -> None:
    """
    Prepares the ffmpeg path and environment variables for Topaz Video AI integration.
    """
    topaz_path = cs.settings.get("topazAIPath", "")
    if not topaz_path:
        return  # Nothing to do if not set

    # Step 1: Get directory from path
    topaz_dir = Path(topaz_path)
    if not topaz_dir.is_dir():
        topaz_dir = topaz_dir.parent

    # Step 2: Ensure ffmpeg.exe exists in the directory
    ffmpeg_path = Path(str(topaz_dir / "ffmpeg.exe"))
    if not ffmpeg_path.is_file():
        raise FileNotFoundError(f"ffmpeg.exe not found in {topaz_dir}")

    # Step 3: Set cs.clipper_paths.ffmpegPath
    cs.clipper_paths.ffmpegPath = str(ffmpeg_path).replace("\\", "/")

    # Step 4: Set environment variables for Topaz model directories
    model_data_dir = cs.settings.get("topazModelDataDir", "")
    model_dir = cs.settings.get("topazModelDir", "")
    if not model_data_dir or not model_dir:
        raise ValueError("Both topazModelDataDir and topazModelDir must be set in settings.")

    os.environ["TVAI_MODEL_DATA_DIR"] = model_data_dir
    os.environ["TVAI_MODEL_DIR"] = model_dir
    logger.debug(f"Topaz model data directory set to: {model_data_dir}")
    logger.debug(f"Topaz model directory set to: {model_dir}")
    # CUDA optimizations
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # Adjust as needed for your setup
    os.environ["CUDA_DEVICE_MAX_CONNECTIONS"] = "2"


def setupDepPaths(cs: ClipperState) -> None:
    settings = cs.settings
    cp = cs.clipper_paths

    if getattr(sys, "frozen", False):
        cp.ffmpegPath = "./bin/ffmpeg"
        cp.ffprobePath = "./bin/ffprobe"
        cp.ffplayPath = "./bin/ffplay"
        cp.ytdlPath = "./bin/yt-dlp"

        if sys.platform == "win32":
            cp.ffmpegPath += ".exe"
            cp.ffprobePath += ".exe"
            cp.ffplayPath += ".exe"
            cp.ytdlPath += ".exe"

        if sys.platform == "darwin":
            cp.ytdlPath += "_macos"

            certifi_cacert_path = certifi.where()
            os.environ["SSL_CERT_FILE"] = certifi_cacert_path
            os.environ["REQUESTS_CA_BUNDLE"] = certifi_cacert_path

    if settings["ytdlLocation"]:
        cp.ytdlPath = settings["ytdlLocation"]

    prepareTopazFFmpeg(cs)


def setupOutputPaths(cs: ClipperState) -> None:
    settings = cs.settings
    cp = cs.clipper_paths
    cp.clipsPath += f'/{settings["titleSuffix"]}'

    os.makedirs(f"{cp.clipsPath}/temp", exist_ok=True)
    settings["downloadVideoPath"] = f'{cp.clipsPath}/{settings["downloadVideoNameStem"]}'


if __name__ == "__main__":
    main()
