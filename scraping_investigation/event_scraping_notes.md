# Reverse engineering the API call to get more events that the 'see more' button uses

## relevant code pieces

### html element

```html
<div class="see-more see-more-article-listing-section" data-url="/en/section-articles-see-more-ajax?dateoff=" data-offset="6" data-see-more-limit="4" data-form-id="mtgo-decklists-custom-search">
<p><a href="javascript:void(0);"><span>See more archives</span></a></p> </div>
```

## javascript

see mx.js lines 212-290

## thoughts

endpoint contains ```/en/section-articles-see-more-ajax?dateoff=```

I have to assume this is the beginning of the endpoint with the domain being magic.wizards.com, but I could be wrong

# Ok you know what fuck this I'm just going to intercept it with wireshark

```/en/section-articles-see-more-ajax?dateoff=&l=en&f=9041&search-result-theme=&limit=4&fromDate=&toDate=&sort=DESC&word=&offset=6```

BOOM BABY (shoutout to Chris Greer's youtube channel)

so I think the final endpoint should be:

```https://wizards.magic.com/en/section-articles-see-more-ajax?dateoff=&l=en&f=9041&search-result-theme=&limit=4&fromDate=&toDate=&sort=DESC&word=&offset=6```

ok that doesn't actually work and I will have to dig into the packet a bit more, but this is progress. I think I can ignore the js from now on.