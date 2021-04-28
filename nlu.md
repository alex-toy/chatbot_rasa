## intent:greet
- hi
- hey
- hello
- good morning
- how are you
- hola


## intent:buy_phone_laptop
- I would like to buy a [phone](category)
- I want to buy a [laptop](category)
- Please suggest me a good [laptop](category)
- I wanted to purchase a [phone](category)
- Can you recommend me a [laptop](category)
- Can you suggest me a [laptop](category)
- I'm interested in purchasing a [phone](category)
- I wanna buy a [mobile]{"entity" : "category", "value" : "phone"}
- give me some recommandations for [mobile]{"entity" : "category", "value" : "phone"}


## intent:latest_news_phones_laptop
- whats the latest news with [phones](category)
- can you tell me about the trends regarding [phones](category)
- what's going on in the tech world for [laptops](category)
- can you show me the trends in [laptops](category)
- show me the latest news for [mobiles]{"entity" : "category", "value" : "phone"}
- update me on the latest [mobiles]{"entity" : "category", "value" : "phone"} news
- Any new releases for [mobiles](category)


## intent:goodbye
- goodbye
- see you
- ciao
- bye bye
- bye
- talk to you later
- see you around


## synonym:phone
- mobile
- mobiles
- mobile phone


## synonym:laptop
- computer
- laptops
- computers


## lookup:category
data/lookup_tables/category.txt