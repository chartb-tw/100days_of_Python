## The RealTimeTrains API "copy" site

This site uses the [RealtimeTrains API](https://www.realtimetrains.co.uk/about/developer/) and is designed around two (accessbile) pages. The first is the homepage, and the second fetches data on train departures based on the [CRS or TIPLOC code](http://www.railwaycodes.org.uk/crs/crs0.shtm) being passed in.

This was made as a "quick and easy" solution for the day 95 exercise of the course, and uses the basic template that I had designed. The site hasn't been set up to handle exceptions well (nor do I really intend on adding that functionality, unless it comes as part of learning something I need to). There is also the lazily implemented search for a specific train, which uses the UID (not the four character identity!) e.g. as below:

![Screenshot 2022-06-06 at 03 39 47](https://user-images.githubusercontent.com/74368960/174228645-4088c543-f22e-4649-9076-a64bc334de39.png)

Hopefully it serves as an example of how to use APIs and the responses that are gained from them! (The site of course is not designed for any true production use whatsoever, just a bit of fun!)

(s, f)

