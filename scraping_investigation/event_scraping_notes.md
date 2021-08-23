# Reverse engineering the API call to get more events that the 'see more' button uses

## relevant code pieces

### html element

```html
<div class="see-more see-more-article-listing-section" data-url="/en/section-articles-see-more-ajax?dateoff=" data-offset="6" data-see-more-limit="4" data-form-id="mtgo-decklists-custom-search">
<p><a href="javascript:void(0);"><span>See more archives</span></a></p> </div>
```

## Endpoint intercepted from wireshark
When I click the 'see-more' button my browser makes a GET request to the following endpoint:
```/en/section-articles-see-more-ajax?dateoff=&l=en&f=9041&search-result-theme=&limit=4&fromDate=&toDate=&sort=DESC&word=&offset=6```

so I think the final endpoint should be:

```https://wizards.magic.com/en/section-articles-see-more-ajax?dateoff=&l=en&f=9041&search-result-theme=&limit=4&fromDate=&toDate=&sort=DESC&word=&offset=6```
