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
    <h1>Hello  {name}</h1>
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
    <h1>Dear {name}</h1>
    <p>Hope you're doing very well.</p>
    <p>Do you know a bunch of doctors are using WhatsApp or Telegram for serious medical chats?
         Yes, it's happening. And we thought, "There's got to be a better way!" We create <b>TERAL, the chat for Doctors</b> </p>
    <p>We've crafted TERAL with loads of love (and tech wizardry!) to be the go-to, ultra-secure chat platform just 
        for healthcare professionals. It's more than just chatting – it's about speeding up responses, sharing clinical 
        insights instantly, avoiding those pesky extra costs from unnecessary referrals, and overall, just making the whole 
        healthcare system a bit smarter and a lot safer..</p>
    <p>Excited? So are we! Let’s dive deeper into how TERAL can make a world of difference. </p>


    <p>I’ve attached our <b>investor deck</b> and a demo for a deeper dive.</p>
    <p>Let's schedule a meeting soon!</p>
    <p>Cheers,</p>

    <p>David Calderón<br>
    CEO<br>
    Teral</p>

    <br>
    <a href="https://youtu.be/a2crkSQyjXA">click for more information</a><br>
    <a href={pdf_link}>introducing PDF</a>


    </body>
    </html>
    '''

    T = [html1,html2,html3]    
    texte = T[version]
    return texte

#print(text("evann",1,"0"))
