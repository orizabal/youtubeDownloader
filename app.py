import pytube
import inquirer

question = [
    inquirer.List(
        'try_again',
        message='Would you like to try again?',
        choices=['Yes', 'No']
    )
]

SAVE_PATH = '../Downloads'

print('\nWelcome to the YouTube Downloader!\n')

def end_program():
    print('\nThank you for using the YouTube Downloader!\n\n')
    exit()

def download_video(vid):
    d_video = vid.streams.get_highest_resolution()

    try:
        d_video.download(SAVE_PATH)
    except:
        print('There was an issue saving the video :(\n')

    end_program()

def handle_error():
    print('\nThere was an issue getting that video :(\n')
    if inquirer.prompt(question) == 'No':
        end_program()
    else:
        get_video()

def get_video():
    link = input('\nEnter the link of the YouTube video you want to download: ')

    try:
        video = pytube.YouTube(link)
    except:
        handle_error()
    
    download_video(video)

get_video()


