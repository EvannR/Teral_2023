

def text(name,version,pdf_link):
    html1 = f'''
    <html>
    <body>
    <h1>Dear {name}</h1>
    <p>I recently came across your investment profile on Crunchbase and was compelled to reach out.</p>
    <p>We are in the process of developing a specialized chat platform dedicated for doctors. 
    As we gear up for our seed round next month, I'm eager to discuss potential investment 
    opportunities with you. Could you provide insights on your current investment interests 
    and how you typically review new deals?</p>

    <p>Attached, you'll find a brief video showcasing our platform.<p>

    <p>Thank you for your consideration.</p>

    <p>David Calderón<br>
    CEO<br>
    Teral</p>

    <br>
    <a href="https://youtu.be/a2crkSQyjXA">click for more information</a><br>
    <a href={pdf_link}>introducing PDF</a>


    </body>
    </html>
    '''



    html2 = f'''
    <html>
    <body>
    <h1>Hello {name}</h1>
    <p>I hope this message finds you well. Your investment portfolio on Crunchbase caught my attention.</p>

    <p>We are poised to launch a unique chat platform tailored specifically for medical professionals. 
    With our seed round slated for next month, we're seeking discerning investors like yourself. 
    May I inquire about your current investment strategies and your evaluation process for new ventures?</p>

    <p>For a clearer understanding of our platform, I've attached a short video demonstration.</p>

    <p>Your time and consideration are greatly appreciated.<p>

    <p>David Calderón<br>
    CEO<br>
    Teral</p>

    <br>
    <a href="https://youtu.be/a2crkSQyjXA">click for more information</a><br>
    <a href={pdf_link}>introducing PDF</a>


    </body>
    </html>
    '''



    html3 = f'''
    <html>
    <body>
    <h1>Greetings {name}</h1>
    <p>Your esteemed profile on Crunchbase resonated with our company's vision and aspirations.</p>
    <p>We're at the forefront of introducing a dedicated chat platform for doctors,
      and our seed round is imminent. I'm interested to understand if this aligns with your current 
      investment focus. Could you share how you approach new deals and review pitch decks?</p>


    <p>I've enclosed a video to provide a succinct overview of our platform.</p>
    <p>Thank you in advance for your consideration.</p>

    <p>David Calderón<br>
    CEO<br>
    Teral</p>

    <br>
    <a href="https://youtu.be/a2crkSQyjXA">click for more information</a><br>
    <a href={pdf_link}>introducing PDF</a>


    </body>
    </html>
    '''

    html4 = f'''
    <html>
    <body>
    <h1>Hy {name}</h1>
    <p>Stumbled upon your profile on Crunchbase and, gotta say, I’m impressed.</p>

    <p>We're in the midst of shaping up a game-changing chat platform exclusively for doctors. 
    And guess what? Seed round's right around the corner. Are you still on the prowl for some 
    groundbreaking investments? How do you usually dive into deals or take a look at decks?</p>

    <p>Oh, and check out this quick video I’ve attached. It’s our baby in action!</p>

    <p>Catch you later and thanks for giving this a glance!</p>

    <p>David Calderón<br>
    CEO<br>
    Teral</p>

    <br>
    <a href="https://youtu.be/a2crkSQyjXA">click for more information</a><br>
    <a href={pdf_link}>introducing PDF</a>


    </body>
    </html>
    '''


    html5 = f'''
    <html>
    <body>
    <h1>Hy {name}</h1>
    <p>Your Crunchbase profile? Seriously cool.</p>

    <p>Here's the scoop: we’re whipping up a chat platform, but not just any platform – one designed for our life-saving doctors. Seed round’s on the horizon. Got a moment to chat about investments? How do you typically scope out new deals or decks?</p>

    <p>PS: Don’t miss the video attachment. It's a sneak peek of our magic.</p>

    <p>Cheers and thanks for the peek!</p>

    <p>David Calderón<br>
    CEO<br>
    Teral</p>

    <br>
    <a href="https://youtu.be/a2crkSQyjXA">click for more information</a><br>
    <a href={pdf_link}>introducing PDF</a>


    </body>
    </html>
    '''


    html6 = f'''
    <html>
    <body>
    <h1>Hy {name}</h1>
    <p>Caught a glimpse of your investor mojo on Crunchbase – pretty stellar!</p>

    <p>Here’s what we’ve got cooking: a chat platform, tailor-made for doctors. With our seed round fast approaching, I’m curious – are you hunting for the next big thing? What's your go-to method for reviewing deals or decks?</p>

    <p>There’s a video attached here. It's our platform doing its thing, do check it out!</p>

    <p>Thanks for the look-see!</p>


    <p>David Calderón<br>
    CEO<br>
    Teral</p>

    <br>
    <a href="https://youtu.be/a2crkSQyjXA">click for more information</a><br>
    <a href={pdf_link}>introducing PDF</a>


    </body>
    </html>
    '''

    T = [html1,html2,html3,html4,html5,html6]    
    texte = T[version]
    return texte
