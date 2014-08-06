price-of-weed
=============

Scrapes PriceofWeed.com every six hours.

# Cronjobs

### Scape for data, four times daily
```
0 */6 * * * make -C /home/ubuntu/price-of-weed/
```

### Generate daily json
```
0 12 * * * bash /home/ubuntu/price-of-weed/daily.sh
```