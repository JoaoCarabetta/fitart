# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pathlib import Path
import yaml
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import random


def edit_clip(clip, config):

    for func, params in config.items():

        func_args = {}  # func_args = {'speedx': 2}
        for param, rang in params.items():
            func_args[param] = random.uniform(rang["from"], rang["to"])
        print(func, func_args)

        clip = getattr(vfx, func)(clip, **func_args)

    return clip


def edit_video():
    """
    - Trim video
    - Change speed
    - Reverse
    - Add images
    """

    original_path = Path("videos/original/")
    target_path = Path("videos/edited/")

    # load yaml file from configs/first.yaml
    with open("configs/first.yaml", "r") as f:
        config = yaml.load(f)

    # Load all videos from original path in list
    clips = [VideoFileClip(str(file)) for file in original_path.iterdir()]

    clips = [edit_clip(clip, config) for clip in clips]

    final_clip = concatenate_videoclips(clips)
    print(final_clip)
    final_clip.write_videofile(str(target_path / "edited.mp4"))


if __name__ == "__main__":
    edit_video()
