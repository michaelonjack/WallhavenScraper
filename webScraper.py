# Web Crawler
import mechanize
import urllib

def get_wallpapers(url,directory):

    browser = mechanize.Browser()

    browser.set_handle_equiv(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(True)

    browser.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]

    # Create string of html code of requested webpage
    html = browser.open(url).read()
    browser.close()
    # Array to hold image file names+extensions
    images = []

    # Standard format of how the image file is stored in html of wallhaven website
    # Only missing the unique image extension at the end
    standard = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'

    #End of webpage html
    endIndex = len(html)
        
    # Initialize the current index to position in html near the image files
    currentIndex = html.find('figure  id="thumb-')
    while currentIndex != -1:
        # Create substring of html to hold only relevant code (image files)
        html = html[currentIndex:endIndex]
        # Beginning of unique image extension
        beginExtension = html.find('th-') + 3
        # End of unique image extension
        endExtension = html.find('"', beginExtension)
        # Extension of unique image file
        extension = html[beginExtension:endExtension]
        # Create full image file name
        currentImage = standard + extension
        # Parse html so that the previously acquired image address is excluded
        html = html[endExtension:endIndex]

        # Add the current image to the array of images
        images.append(currentImage)
        # Set currentIndex for the next loop iteration
        currentIndex = html.find('figure  id="thumb-')

    # Print image file names to verify correct parsing
    for i in range(len(images)):
        print(images[i])


    print('Downloading images..')


    count = 0
    for pic in images:
        count += 1
        print("Image " + str(count))
        # Retrieve the current pic and store in specified local location
        urllib.urlretrieve(pic, directory + 'wallbase_img_' + str(count) + '.jpg')
    
    print('Download complete.')



if __name__ == "__main__":

    base_url = 'http://alpha.wallhaven.cc/search?q='
    user_direc = raw_input('Enter the directory path to where you would like to store your images: ')
    user_search = raw_input("Enter the type of wallpaper you're searching for (ex. 'batman'): ")
    user_search = urllib.quote(user_search)
    url = base_url + user_search
    print url
    get_wallpapers(url,user_direc)

