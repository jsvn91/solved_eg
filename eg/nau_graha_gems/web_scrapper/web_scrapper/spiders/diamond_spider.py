from pathlib import Path

import scrapy


class BrillantDiamondSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [ 
                    'https://www.brilliantearth.com/lab-diamonds/list/?shapes=Round', 
                    ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def prep_url(self, url), cuts = 'cuts=Fair%2CGood%2CVery%20Good%2CIdeal%2CSuper%20Ideal'):
            url_items = [, 
                        
                        ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
