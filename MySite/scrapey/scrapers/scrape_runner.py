"""High level functions to run my scrapers. """

from .class_library import AswathScraper, EugeneScraper, StratecheryScraper, CollaborativeScraper,\
    OSAMScraper, AmnesiaScraper, GatesScraper 

# def scrape_new_data():

    # scrapers = (AswathScraper(), EugeneScraper(), StratecheryScraper(), CollaborativeScraper(),
    # OSAMScraper(), AmnesiaScraper(), GatesScraper())

    # scrapers = (GatesScraper(), )
    # scrapers = []

    # for scraper in scrapers:
    #     print(f'About to try to scrape: {scraper.NAME}')
    #     # try:
    #     scraper.get_new_posts()

        # except:
        #     print(f'Failed somewhere for {scraper.NAME}')

