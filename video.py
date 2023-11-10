import requests
import subprocess
import os 

text = """

"""



## downloading ts files
playlist_lines = text.split('\n')

ts_urls = [line for line in playlist_lines if line.endswith('.ts')]

command = f'mkdir tsfiles'
subprocess.run(command, shell=True)
for i, ts_url in enumerate(ts_urls):
    ts_response = requests.get(ts_url)
    with open(f"tsfiles/tssegment_{i}.ts", 'wb') as ts_file:
        ts_file.write(ts_response.content)



## how many files
n = os.listdir("tsfiles/")

## the order of files
file_list = [f"tsfiles/tssegment_{count}.ts" for count in range(len(n))]

## generating ffmpg command and export .mp4
input_files = "|".join(file_list)
output_file = "output.mp4"
command = f'ffmpeg -i "concat:{input_files}" -c copy {output_file}'
subprocess.run(command, shell=True)

## remove downloaded files
subprocess.run("rm -rf tsfiles", shell=True)





