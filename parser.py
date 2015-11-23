from datetime import datetime
import requests
import time

__author__ = 'GANGESHWAR'

def get_content():
    try:
        url = 'http://results.vtu.ac.in/'
        page = requests.get(url)
        #print(page.text)
        string = "M.Tech II / III Semester Results".lower()
        str1 = "B.E/B.Tech III/IV Semester Results Announced for Belgaum & Gulbarga Region".lower()
        string1 = "B.E/B.Tech III/IV Semester Results Announced for All Region".lower()
        string4 = "B.E/B.Tech III / IV Semester Results Announced for All Region".lower()
        string2 = "B.E/B.Tech III/IV Semester Results Announced for Bangalore & Mysore Region".lower()
        string3 = "B.E/B.Tech III / IV Semester Results Announced for Bangalore & Mysore Region".lower()
        time1 = datetime.now().time()
        if (page.text.lower().find(string1) != -1) | (page.text.lower().find(string2) != -1)\
                | (page.text.lower().find(string3) != -1) | (page.text.lower().find(string4) != -1):
            print time1.isoformat()+'  Results announced! Goto http://results.vtu.ac.in/ \nAll the Best!'
            return False
        else:
            print time1.isoformat()+ ' Not yet announced!'
            return True
    except Exception, e:
        time1 = datetime.now().time()
        print time1.isoformat()+ "Exception found : " + e.message
    finally:
        pass

    return True

def main():
    print "Developed by K.Gangeshwar"
    print "Checking VTU 3rd Sem results announcement..." \
          "\nNote: Don't close this program. This program checks for results from VTU website every 5 seconds."
    ret = True
    while ret:
        ret = get_content()
        time.sleep(5)
    print "You may close this program!"

if __name__ == '__main__':
    main()
