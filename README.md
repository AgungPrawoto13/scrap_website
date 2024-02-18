# SCRAPING WEBSITE USING SELENIUM AND BEAUTIFULSOUP4
This project aims to gather data related to quick count results and regional elections (pilkada) from websites using web scraping techniques.

## Tools
### Mozilla Driver
A driver specifically designed for interacting with the Mozilla Firefox browser. Used in web automation testing and data scraping with Selenium.

### Selenium:
An automation tool for web testing and data scraping. Supports various programming languages such as Python, Java, and others.
Interacts with browsers to automate actions like clicking, filling forms, and navigation.

### Beautiful Soup:
A Python library for data scraping and HTML/XML parsing.Facilitates information extraction from HTML and XML documents.
Versatile in extracting and manipulating data from websites.

## Scope:
### 1. Web Scraping Quick Count Data:
Using Selenium, this script is designed to extract quick count data from the target website.
Collected data includes information such as candidate names, vote counts, party names, and other relevant details.

### 2. Web Scraping Regional Election List:
Using JavaScript to fetch all links at the city/regency level, followed by Beautiful Soup 4 to extract links for the regional election list.
The obtained links serve as references for subsequent data retrieval.

## Getting Started
Make sure you have downloaded the mozilla drivers, here are the links
https://github.com/mozilla/geckodriver/releases

I am using the Mozilla driver because it's simpler and doesn't require downgrading or updating. If using Google Chrome, the driver version needs to be adjusted to match the version of Google Chrome.

this target link 
quick count pilkada 
https://www.cnnindonesia.com/pemilu2024/pilpres-quickcount

list of regional elections (pilkada)
https://id.wikipedia.org/wiki/Daftar_pemilihan_umum_kepala_daerah_di_Indonesia_2024#Tingkat_provinsi

I am scraping regional election (pilkada) data at the provincial and city/regency levels, and I need to obtain all the links. Therefore, I have prepared a JavaScript script to retrieve all the links at the city/regency level. These links will be subsequently requested and scraped using Beautiful Soup

### Setup
1. **Clone This Repo:**
   ```bash
   git clone https://github.com/AgungPrawoto13/scrap_website.git
   ```

2. **Open Link Website Pilkada**
   Then select the three dots in the upper right corner, choose "More tools," and select "Developer Tools," or use Ctrl + Shift + I. Next,
   choose the console and run the following script
   ```bash
    content_id = document.getElementById('mw-content-text')

    for (let x = 1; x <= 37; x++) {
        ulElement = content_id.getElementsByTagName("ul")[x]
    
        if(ulElement){
            anchor = ulElement.getElementsByTagName('a')
            
            for(let y = 0; y <= anchor.length; y++){
    
                if(anchor[y] != undefined){
                    console.log(anchor[y].href)
                }
            }
        }
    }
   ```
   This script will retrieve all the links available at the city/regency level, then copy those links and save them into an Excel file
