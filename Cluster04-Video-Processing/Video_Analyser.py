import os
import json
import subprocess
import shutil
from pathlib import Path


def format_file_size(size_in_bytes):
    """Convert bytes into readable file size."""

    size = float(size_in_bytes)

    units = ["Bytes", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


def format_duration(seconds):
    """Convert seconds into HH:MM:SS."""

    try:
        seconds = float(seconds)

        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = seconds % 60

        return f"{hours:02}:{minutes:02}:{seconds:06.3f}"

    except:
        return "Not Available"


def check_ffprobe():
    """Check FFprobe availability."""

    return shutil.which("ffprobe") is not None


def get_video_metadata(video_path):
    """Extract metadata using FFprobe."""

    command = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        video_path
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return json.loads(result.stdout)


def get_stream(streams, stream_type):

    for stream in streams:
        if stream.get("codec_type") == stream_type:
            return stream

    return None


def print_tag(label, value):

    if value is None or value == "":
        value = "Not Available"

    print(f"{label:<20}: {value}")


def analyze_video(video_path):

    if not os.path.exists(video_path):
        print("Error: Video file not found.")
        return

    if not check_ffprobe():
        print("Error: FFprobe not installed.")
        return


    try:

        metadata = get_video_metadata(video_path)

        file_info = Path(video_path)

        file_size = os.path.getsize(video_path)

        format_data = metadata.get("format", {})

        streams = metadata.get("streams", [])


        video_stream = get_stream(streams, "video")
        audio_stream = get_stream(streams, "audio")


        print("\n================================")
        print(" VIDEO METADATA REPORT ")
        print("================================")


        print("\nBasic Information")
        print("--------------------------------")

        print_tag(
            "File Name",
            file_info.name
        )

        print_tag(
            "File Size",
            format_file_size(file_size)
        )


        print_tag(
            "Container",
            format_data.get("format_long_name")
        )


        print_tag(
            "Duration",
            format_duration(format_data.get("duration"))
        )


        # VIDEO SECTION

        print("\nVIDEO")

        print("--------------------------------")


        if video_stream:

            width = video_stream.get("width")
            height = video_stream.get("height")

            print_tag(
                "Resolution",
                f"{width}x{height}"
                if width and height
                else None
            )


            fps = video_stream.get("r_frame_rate")

            print_tag(
                "Frame Rate",
                fps
            )


            print_tag(
                "Bit Rate",
                (
                    f"{int(video_stream.get('bit_rate'))/1000:.2f} kbps"
                    if video_stream.get("bit_rate")
                    else None
                )
            )


            print_tag(
                "Codec",
                video_stream.get("codec_long_name")
            )


        else:
            print("No Video Stream Found")


        # AUDIO SECTION

        print("\nAUDIO")

        print("--------------------------------")


        if audio_stream:


            print_tag(
                "Codec",
                audio_stream.get("codec_long_name")
            )


            print_tag(
                "Channels",
                audio_stream.get("channels")
            )


            print_tag(
                "Sampling Rate",
                (
                    f"{audio_stream.get('sample_rate')} Hz"
                    if audio_stream.get("sample_rate")
                    else None
                )
            )


            print_tag(
                "Bit Rate",
                (
                    f"{int(audio_stream.get('bit_rate'))/1000:.2f} kbps"
                    if audio_stream.get("bit_rate")
                    else None
                )
            )


        else:

            print("No Audio Stream Found")


        # METADATA SECTION

        print("\nMETADATA")

        print("--------------------------------")


        tags = format_data.get("tags", {})


        if tags:

            for key, value in tags.items():

                print_tag(
                    key,
                    value
                )

        else:

            print("No Metadata Available")


        print("\n================================")
        print("REPORT COMPLETED")
        print("================================")


    except Exception as error:

        print(
            f"Error while processing video: {error}"
        )



def main():

    print("=" * 40)
    print("VIDEO FILE ANALYZER")
    print("=" * 40)


    video_path = "video.mp4"


    video_path = video_path.strip('"').strip("'")


    analyze_video(video_path)



if __name__ == "__main__":
    main()
