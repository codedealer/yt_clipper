from fractions import Fraction
from typing import Optional, Tuple

from clipper.clipper_types import DictStrAny


def getFfmpegVideoCodecArgs(
    videoCodec: str,
    cbr: Optional[int],
    mp: DictStrAny,
    mps: DictStrAny,
    qmax: int,
    qmin: int,
) -> Tuple[str, str, str]:
    if videoCodec == "h264_nvenc":
        return getFfmpegVideoCodecH264Nvenc(cbr=cbr, mp=mp, mps=mps, qmax=qmax, qmin=qmin)

    raise ValueError(f"Only h264_nvenc is supported in nv_clipper: {videoCodec} was supplied")


def getFfmpegVideoCodecH264Nvenc(
    cbr: Optional[int],
    mp: DictStrAny,
    mps: DictStrAny,
    qmax: int,
    qmin: int,
) -> Tuple[str, str, str]:
    fps_arg = ""
    if not mps["h264DisableReduceStutter"]:
        if mps["minterpFPS"] is not None:
            fps_arg = f'-r {mps["minterpFPS"]}'
        elif not mp["isVariableSpeed"]:
            fps_arg = f'-r ({mps["r_frame_rate"]}*{mp["speed"]})'

    if mp["isVariableSpeed"]:
        fps_arg = "-fps_mode vfr"

    sdr_args = "-pix_fmt cuda"
    # h264_nvenc does not support 10-bit HDR output
    hdr_args = "-pix_fmt cuda -color_primaries bt2020 -color_trc smpte2084 -colorspace bt2020nc"

    dynamic_range_args = sdr_args
    if mps["enableHDR"]:
        dynamic_range_args = hdr_args

    video_codec_args = " ".join(
        (
            f"-c:v h264_nvenc",
            f"-movflags write_colr",
            dynamic_range_args,
            # vbr_hq is deprecated
            "-rc vbr" if cbr is None else "-rc cbr",
            # h264_nvenc cq should be equivalent to h264 crf and is between 0 and 51 (same as qp)
            # h264_nvenc doesn't support modes like constrained encoding / VBV (Video Buffering Verifier)
            # so we remove the -cq option when in cbr mode
            f"-cq {mps['crf']}" if cbr is None and mps["targetSize"] <= 0 else "",
            f"-qmin 3 -qmax {qmax}" if mps["targetSize"] <= 0 else "",
            f'-b:v {mps["targetMaxBitrate"]}k' if cbr is None else f"-b:v {cbr}MB",
            f'-maxrate {mps["targetMaxBitrate"]*2}k' if cbr is None else f"-maxrate {cbr*2}MB",
            f'-force_key_frames 1 -g {mp["averageSpeed"] * Fraction(mps["r_frame_rate"])}',
            # video_track_timescale = 2^4 * 3^2 * 5^2 * 7 * 11 * 13 * 23, max is ~2E9
            f" -video_track_timescale 82882800",
            "-qcomp 0.9",
            # NVENC specific settings - optimized for latency tolerant high quality encoding
            "-tune hq",
            "-preset p6",
            # There are no devices that support more than 4 B-frames currently
            "-bf 4",
            # rc-lookahead default is 40, diminishing returns beyond 60
            # although expensive, it may be worth it for gpu encodes which often have lower quality
            "-rc-lookahead 40",
            "-spatial-aq 1",
            "-aq-strength 12",
            "-keyint_min 1",
        ),
    )

    video_codec_input_args = "-hwaccel cuda -hwaccel_output_format cuda"
    video_codec_output_args = " ".join(("-f mp4", fps_arg))
    return video_codec_args, video_codec_input_args, video_codec_output_args
