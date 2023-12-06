from moviepy.editor import VideoFileClip

def mp4_to_mp3_converter(inp,out):
    v = vf(inp)
    a = v.audio
    
    a.wa(out,codec='mp3')
    
    a.close()
    video.close()
    
if __name__ == "__main__":
    inp = 'input_path_of_mp4file'
    out = 'output_path_of_mp3file'
    
    mp4_to_mp3_converter(inp,out)
    
    # To run the script = "python mp4_to_mp3_converter.py"  
