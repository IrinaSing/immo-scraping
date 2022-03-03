Inside the folder you can find all the links that were used to scrape the needed information.

After the get_url.py file has ran its course we have a url_links.txt file filled with thousands of links of properties on the website immoweb.be.
We then copy these and input them in a simple Excel worksheet where we remove the duplicate values.

![image](https://user-images.githubusercontent.com/98815092/156535886-9b936823-13d0-4aa2-ac0a-07227e455b08.png)

After this we have a list of unique links to thousands of property listings on the website. We save this in the filtered_url.txt file.
Now we have our basic data to loop over and extract the needed property information through the Main.py file.
