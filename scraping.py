from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="section-1">
        <h3 data-hello="hi">Hello</h3>
        <img src="https://cdn.pixabay.com/photo/2016/03/26/13/09/cup-of-coffee-1280537_960_720.jpg"/>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras interdum vel felis id mattis. Nam nec erat eget eros lacinia porttitor. Integer ultricies dignissim libero, ut vulputate sem egestas ac. In in accumsan elit. Donec placerat tellus eget aliquam vulputate. Aenean sit amet facilisis lacus. Fusce elit tortor, mattis ac ullamcorper in, posuere congue sem. Nunc condimentum nec mi venenatis ullamcorper. Nunc ac cursus purus. Pellentesque quis vehicula sapien.</p>
    </div>

    <div id="section-2">
        <ul class="items">
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 2</a></li>
            <li class="item"><a href="#">Item 3</a></li>
            <li class="item"><a href="#">Item 4</a></li>
            <li class="item"><a href="#">Item 5</a></li>
        </ul>
    </div>

</body>
</html>
"""

# Below initialises BeautifulSoup.
soup = BeautifulSoup(html_doc, "html.parser")

# Below selects the body element in the html_doc variable. We can also select other elements such as head.
# print(soup.body)

# The find method returns only the first instance of the selected element.
find_element = soup.find("div")

# find_all() or findAll() will find every instance of that element and return it in a list.
find_all_divs = soup.find_all("div")

# We can use indexes to be more specific with our search
find_by_index = soup.find_all("div")[1]

# Pass id="" or class_="" into the find method to search by the chosen selector.
find_by_id = soup.find(id="section-1")
find_by_class = soup.find(class_="items")

# Below is how to select attributes values with a json object.
find_attr = soup.find(attrs={"data-hello": "hi"})

# The select method allows us to select by css selectors. Select always returns a list.
select_this_id = soup.select("#section-1")

# If we specify by index, we won't be returned a list
select_this_class = soup.select(".item")[2]

# To get the data within selected tags we use get text. First we find() then we get_text().
get_text = soup.find(class_="item").get_text()

# For loops can be used to iterate over numerous uses of a selector. Then get_text() can be used to get that iterations text
# for item in soup.select(".item"):
    # print(item.get_text())

# When navigating through the data, /n new lines are seen as items in the list thats returned so below renders the following:
# contents = soup.body.contents
# contents_index1 = soup.body.contents[1]
# contents_index2 = soup.body.contents[2]
# contents_index3 = soup.body.contents[3]
# contents_index4 = soup.body.contents[4]
# contents_index5 = soup.body.contents[5]

# Below selects the first section > first element in the section then the next sibling not incl. the /n new line.
contents_index = soup.body.contents[1].contents[1].find_next_sibling()

# Finding previous sibling works in a similar fashion.
prev_sibling = soup.find(id="section-2").find_previous_sibling()

find_parent = soup.find(id="section-1").find_parents()

