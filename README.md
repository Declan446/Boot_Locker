# Boot Locker

**About** I have based my project on a webapp that sells Football boots.I plan to create a clear , easy and well structured web application
so that Foootball enthusiast can find the perfect pair of boots.

**Personal Reasons For Creating This Web Application**
* Trying to find the perfect pair of boots was a long and tedious task when i was younger. Going from shop to shop with my father and not
  really having any idea what boots i was actually looking for.
* My brother has three boys who love playing and watching football. Every six months or so they are asking my brother for a new pair of boots.
  My brother would ask "What pair do you want?" and the answer was always the same "What ever pair Messi or Ronaldo are wearing".

So with all this in mind i decided to build Boot Locker, to take the pain and stress out of finding the perfect pair of boots.

**Business Opportunities**
* Making a percentage of the profit on every pair of boots sold on the app.
* Advertising for Football products
* Advertising for sports brands like Adidas and Nike for example.
* Advertising for teams that are looking for new talent.
* Advertising for Colleges who are offering scholarships.

**Users Benefits**
* The ability to find and buy boots without having to leave the comfort of their homes.
* They are able to create an account and keep track of their sending.
* They will be able to see all of their purchase history.
* They can see what pair of boots the top player are wearing.

# UX Design

The first thing i did in regards to *UX design* is make a list of users who might visit my web application.
* Someone who loves football and wants access to the lastest boots.
* Someone who wants a new pair of football boots but doesnt know what pair they want.
* A football manager looking for boots for his team.
* Parents looking for reasonable priced boots for their teenager.
* A football club looking for boots with the same colours of their team.

**Users Stories**
1. As a user and football player, i would like access to the lastest football boots.
2. AS a user and football player, i would the ability to create an account.
3. as a user and football player, i would like to filter the boots by brand and style.
4. As a user and football player, i would like to login and view my order history.
5. As a user and a parent, i would like to find the boots messi wears for my teenager
6. As a user and manager, i would like to filter the boots by colour to match my teams colour.

# Design

**Theme**
I got my inspiration for my theme from a mini project i did with the *Code Institute*. The mini project was 
thorin and company and in this project they used a bootstrap theme called **Clean Blog**. While using this theme 
in the mini project i found it to be very clear, well structured and easy to navigate. For these reasons i decided 
to use it for my Irish Recipes web application. One major deciding factor for choosing this theme was it was the
only free multi page design on the bootstrap site that i liked. I used a theme because it speeds up the design Process
and leaves less room for errors and display problems. 

**Home Page Image**
For my Home page image i choose a picture of the a fooball stadium. I choose this image because its a familiar image for 
my target User

**Colours**


**Icons**
I used Font Awesome for the icons on the shopping bag and profile.

**Planning**

1. I decided to create a web application on selling football boots that users could find and buy boots with ease.
2. I talked to potential users and found out their needs.
3. Users needs are as follows: fast, easy to navigate and clean clear images of football boots.
4. I then picked my boots i wanted to add to my site (Adidas, Nike and New Balance)
5. Picked my images for my home page.
6. Decided what buttons were going to be in my navbar (Adidas, Nike, New Balance ).
7. Picked the features that the web application would have.
8. Designed my wireframes.
9. Picked my Boots and images.
10. Picked what way i was going to filter the boots.
11. Then i opened gitpod and started coding.

**Wireframes**

![Home page](/boot_locker/wireframes/boot-locker-home.png)

**Models**

![Boots.Brand Model](/media/model_boots.brand.jpg)

# Features

**Nav Bar:** The nar bar has four dropdown buttons and one link button(All Boots, Adidas, Nike, New Balance and Players) 
The nav bar displays as a button when been viewed on a mobile device.

**Search Bar**The search bar allows users to search all the the football boots in the app

**Account** Users have the ability to create a Personal account and it stores all their info and order history

**Shopping Bag** Users can add boots to their shopping bag and get them delivered to their doorstop. The bag also has a running total
so the user will know how much they are spending before checkout.

# Technologies Used
The Boot Locker Web Application main Technologies used were as follows:
* **Django** was the framework for this project
* **Gitpod** was used as the IDE for building Boot Locker web application.
* **GitHub** was used to store the project remotely and always used to deploy the project while in constrcution before deploying to heroku
* **HTML** was used to structure the web pages.
* **CSS** was used for the styling.
* **Phython** was used for alot of the core funtinality
* **JQuery** was used as part  functionality.
* **JavaScript** was used for many features of the app.
* **SQL light** was used as the database to store the boots users order and so on.
* **Imports** Django and json were all imported in to the app .
* **Bootstrap themes** was used for almost everything in this app.
* **Bootstrap** was used for most of the features and functionality.
* **Font Awesome** was used for the icons.
* **Heroku** was used to deploy the final version of the web application.

 # Testing:
 I tested the web application on google chrome, internet explorer, firefox and safari and found no problems displaying the web application
 in any browser. The web application was also tested on all screen sizes.
* Galaxy S5 = No problems.
* Pixel 2 and 2 XL = No problems.
* Iphone 5 = No problems.
* Iphone 6/7/8 = No problems.
* Iphone 5 = No problems.
* Ipads = No problems,

# Deployment

**Deploying to Heroku**
* sign up to heroku
* create new app(irish-recipes)
* connect heroku to Github
* go to gitpod and in the command line type heroku login
* create a requirements.txt file, which contains a list of our dependencies.
* create a Procfile, which is a special kind of file that tells Heroku how to run our project.
* set IP and PORT Config Vars.
* create a secret key in the Config Vars in the heroku settings.
* now go to the git command line and login to heroku.

**Commands to push to heroku**
1. $ Heroku login.
2. $ Heroku ps:scale web=1
3. $ Git push Heroku master.

# Credits:
**Content:**

All the football boots in the app were taking from Sports Direct website.
including name, colour and Price.
https://ie.sportsdirect.com/ - automatic!
[Sports Direct](https://ie.sportsdirect.com/)

**Media:**
All the images for my football boots came from Sports Direct website.
https://ie.sportsdirect.com/ - automatic!
[Sports Direct](https://ie.sportsdirect.com/)

The Home image was taking off google after searching pictuers of football stadium.
https://st2.depositphotos.com/3725083/5769/i/450/depositphotos_57693395-stock-photo-stadium.jpg - automatic!
[Football Stadium ](https://st2.depositphotos.com/3725083/5769/i/450/depositphotos_57693395-stock-photo-stadium.jpg)

**Acknowledgements:**
* I received most of my inspiration for Boot locker from the mini project Boutique Ado in this course i also got 90% of my code from the Boutique Ado project.
I was going to display my home page in a different way but after looking at Sports Direct and lifestyles websites the layout which is 
very similar to Boutique Ado. I decided to take the same approch as Boutique Ado

* I received inspiration for the site from Sports Direct website and lifestyle's website.
