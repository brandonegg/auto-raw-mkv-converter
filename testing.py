import os
import ffmpeg

def process_mkv_file(input_file):
    output_file = input_file.replace('.mkv', '.mp4')
    srt_output_file = input_file.replace('.mkv', '.srt')

    # Get file metadata
    probe = ffmpeg.probe(input_file)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    subtitle_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'subtitle' and 'tags' in stream and stream['tags'].get('language') == 'eng'), None)

    # Check if the video is HDR
    is_hdr = 'color_transfer' in video_stream and video_stream['color_transfer'] == 'smpte2084'

    # Base ffmpeg command
    ffmpeg_command = ffmpeg.input(input_file)
    
    # Video stream conversion
    video = ffmpeg_command.output(output_file, vcodec='libx265', crf=18, preset='slow')
    if is_hdr:
        video = video.filter('scale', '1920x1080')
    video = video.output(output_file, map='0:v')

    # Include all audio tracks
    audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']
    for i, audio_stream in enumerate(audio_streams):
        video = video.output(output_file, map=f'0:a:{i}')

    # Remove all subtitle tracks from the video output
    video = video.output(output_file, sn=0)

    # Run the ffmpeg command to create the mp4 file
    ffmpeg.run(video)

    # Extract English subtitles if available
    if subtitle_stream:
        ffmpeg.input(input_file).output(srt_output_file, map=f'0:{subtitle_stream["index"]}', f='srt').run()

def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mkv'):
                input_file = os.path.join(root, file)
                process_mkv_file(input_file)

if __name__ == '__main__':
    directory = input('Enter the directory to scan: ')
    scan_directory(directory)
