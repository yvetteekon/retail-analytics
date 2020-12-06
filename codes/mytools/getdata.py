import os
import requests

def download_csv(csv_url, outfile_path, csv_outfile_name):
    '''
    Downloads data from url and saves in csv format.

    Parameters
    ----------
    _df : dataframe
        The data set/dataframe to be saved.

    pickle_path : str
        The path to which the data in pickle format should be saved.

    csv_path : str
        The path to which the data in csv format should be saved.

    '''
    # f = open(csv_outfile_name, 'wb')
    # response = requests.get(url)
    # f.write(response.content)
    # f.close()
    # # f.to_csv(csv_outfile_name)

    # f = open(csv_outfile_name, 'wb')
    response = requests.get(csv_url)
    url_content = response.content
    csv_file = open(os.path.join(outfile_path, csv_outfile_name), 'wb')
    csv_file.write(url_content)
    csv_file.close()

#Download zipfile and extract csv from it
#https://books.google.com/books?id=M7pCDwAAQBAJ&pg=PA52&lpg=PA52&dq=how+to+export+data+to+csv+after+downloading+using+url+and+using+write+python+zip+folder&source=bl&ots=8Iqckr5eGH&sig=ACfU3U3CgZlZX65YnonkbvR-LYam4_gcLQ&hl=en&sa=X&ved=2ahUKEwirj96o0P_pAhUDSzABHTTHAakQ6AEwCXoECAkQAQ#v=onepage&q=how%20to%20export%20data%20to%20csv%20after%20downloading%20using%20url%20and%20using%20write%20python%20zip%20folder&f=false    
#https://svaderia.github.io/articles/downloading-and-unzipping-a-zipfile/
#https://stackoverflow.com/questions/37604589/how-can-i-download-a-zipped-file-from-the-internet-using-pandas-0-17-1-and-pytho
#https://likegeeks.com/downloading-files-using-python/