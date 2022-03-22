import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BEKw6JL8aKOqGppD4lpf134TFsm_Pd9nYYWAAvG14yo_YmAJh7_2WZGIm-DFe26rPQ4DJNz6M0F2-y1mXfFkQz6JIiaLNgAvysszoHUAnXH61ESCX6HfzLCX3UIS7E6oFwKiAQ_uDlim'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/SHREESH.K/Documents/kimetsu-no-yaiba-tanjiro-kamado-anime-hd-wallpaper-preview.jpg'
    file_to = '/PC/Downloads/image.jpg'

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
