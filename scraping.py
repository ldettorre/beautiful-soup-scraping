from bs4 import beautifulsoup

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
