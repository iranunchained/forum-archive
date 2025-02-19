# game of trust a web of trust between iranian protesters

*Original topic from 2024-08-21T15:33:38Z*

### Original Post
**Author:** gameoftrust | 2023  
**Date:** 04-26 20:17:11 UTC | #1  

## What is the Game of Trust?

Two things keep a dictatorship alive: "separation" and "silence" among people. (see this video https://www.youtube.com/watch?v=7BRbqNHwu04) The majority of people in Iran oppose the Islamic Republic, whose collective power is much greater than the minority in power. However, there is no reliable way for the people to communicate and coordinate, while the Islamic Republic regime thugs can easily communicate and recognize one another. This puts the people in a weak position.

*The Game of Trust aims to create a secure community of Iranian individuals who oppose the current regime while keeping everyone's identity anonymous, enabling communication, discussions on diverse topics, and coordination.*

## How does the Trust Game work?

To join the system, each person creates an Ethereum address as their digital identity and asks friends and acquaintances within the system to rate them on whether they oppose the Islamic Republic and how trustworthy they are. This way, each person is vouched for by one or more existing members upon entrance. Trust can be transitive, meaning if person "A" trusts person "B," and person "B" trusts person "C," then person "C" is somewhat trustworthy to person "A." Using this principle, you can determine the trustworthiness of any person in the Trust Game based on the trustworthiness of the intermediaries that connect them to you.

*The underlying algorithm for calculating trust in the Trust Game is more complex, and this was a simplified explanation.

We’re using blockchain and decentralized approaches for the system. We have incorporated the EIP-712 TypedData standard in our system to enable users to interact with the system by signing TypedDatas, without the requirement of directly sending a transaction on the blockchain. This approach eliminates the need for users to pay fees, simplifying the onboarding process. Additionally, users can utilize fresh Ethereum addresses to interact with the system, ensuring privacy is maintained. The project's source code is available [here](https://github.com/gameoftrust/).

## What are the applications of the Trust Game?

* Creating and managing anonymous transferable groups in existing social and messaging platforms and using the power of the web of trust and blockchain to keep spammers, government agents, or any unwanted actors out.
* Distributing information and news through trustworthy channels to those who need it, away from the prying eyes of the regime.
* Collective decision-making using various polls and voting methods, forming online communities or political parties, and coordinating protests. (see this post: https://t.me/rzgtrader/14796)
* Identifying genuine protesters and strikers in need of financial aid and directly helping them.
* Fighting the government’s internet censorship attempts and enabling people to access free internet (e.g., distributing VPN configurations without posting them publicly or finding trustworthy sellers to buy Starlink dishes.)
* Verifying the trustworthiness of someone who has posted a video, photo, or report, thus preventing the spread of misinformation by the government
* And more…

---

### Reply #1
**Author:** babri | 2023  
**Date:** 05-04 16:25:14 UTC | #2  

I think this is a promising idea. Would be open to supporting it if we can understand it more. 

I'm having a bit of difficulty thinking through how this'd actually prevent state actors from infiltrating the system. I.e. why can't the basijis join the system and tell the network about trustworthy their comrades are. 

Additionally, can you share a bit about the tooling that is needed to operate such a system. Do you see this system plugging into something like Lens?
What kind of wallet infrastructure would folks need?
Are you planning on promoting the tool and onboarding users? Or are you simply building it as pure technology.

---

### Reply #2
**Author:** ameen | 2023  
**Date:** 05-05 14:25:49 UTC | #3  

I like the idea! I think it could be cool to have public, anonymous, yet still high trust communications channels to share information and facilitate the democratic process in Iran and even internationally!

I also agree with Babri - there doesn't seem to be anything stopping one person from endorsing a whole lot of users (or sybil attacking and pretending to be a lot of users). How can a network mitigate attempts at hostile takeovers?

In addition to answering Babr's other questions, please add your documentation to the github and provide instructions for how one would use the software!

---

### Reply #3
**Author:** gameoftrust | 2023  
**Date:** 05-06 20:33:57 UTC | #4  

Hi @babri @ameen

Thank you for your interest in our project. We have a Persian document for the system that covers more aspects of the product, which you can find here:
https://telegra.ph/Game-of-Trust-04-26

Regarding your question on why Basijis cannot join the system to endorse their comrades, we would like to clarify that our system is designed to assess multiple aspects of a person's character and behavior beyond just trustworthiness. Specifically, we ask the following questions:

1. Is this person aligned against the Islamic Republic?
2. Is this person honest?
3. "This person does not violate collective rights for their own interest", is that true?
4. To what extent can we rely on this person's judgment and opinion when it comes to assessing other people's character?

The first question is the main question that determines whether someone can be in the bot's main community, and the second and third question is for determining whether this person is trustworthy. So, a trustworthy Basiji will not be able to join the system because they do not score highly on the main question. The last question determines the weight of this person's endorsements in calculating the results for other questions for the people in the graph.

Another important thing to consider is that when you are looking at someone's profile in the bot, we show how much you can trust them and if there is a trust path from you to that person. So, for example, if I highly trust someone in the network but you don't trust me, that person can join my group, but they can't join your group.
So, if a thousand Basiji start endorsing each other, it won't affect you if they're not endorsed by the people you trust.

Moreover, our trust algorithm is in its early stages, and we plan to continue improving it based on the data we gather.

We have also provided the option for users to customize the algorithm and questions used in their community, giving them more control over the system's functionality. 

As for the tooling required to operate the system, we have started with a Telegram bot since it is a popular messenger app in Iran. Users can connect their wallet to the bot using WalletConnect. The bot is currently live and can be accessed at https://t.me/irgotbot. However, to participate, you need to be trusted by someone already in the Game of Trust network. We will soon release an update that will allow users to create channels and invite their trustworthy friends, even if they are not part of the existing trust network. Once the Telegram bot gets fit to the use case and works fine, we can easily integrate it with other social media platforms (e.g., Discord, Lens, etc.).

We are continuously updating the software based on user feedback, and we plan to provide deployment instructions on the GitHub repository once we reach a stable version.

---

### Reply #4
**Author:** EVOO | 2023  
**Date:** 08-21 01:06:57 UTC | #5  

Thanks for the proposal. I completely agree with the premise and the need to bootstrap trust, which is what you are describing. It is the basis of the self-sovereign identity model which has many working groups, is part of the standards organizations and IMO the most important solution that's needed. I have previously worked in this area and I am sure it has advanced since. Because the risk is so high here I'd require peer review by relevant researchers in the field. Has your work been reviewed? I am sure it find great interest in the DI community and would return valuable suggestions.
  Ref:  https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/ThePathToSelf-SovereignIdentity.md

---

### Reply #5
**Author:** gameoftrust | 2023  
**Date:** 08-21 14:42:20 UTC | #6  

Hi @EVOO 

Thanks for your comment and interest in Game of Trust.

We were in touch with experts and asked for review on both our code and our idea. We are open to any suggestions on any aspects of our idea and product. Our contract design is simple and all of our codes can be found here: https://github.com/gameoftrust/

We're currently working to improve the idea, both on the technical side and the product side.

---

### Reply #6
**Author:** root | 2023  
**Date:** 08-23 04:01:30 UTC | #7  

[quote="gameoftrust, post:6, topic:48"]
Our contract design is simple and all of our codes can be found here: [gameoftrust · GitHub](https://github.com/gameoftrust/)
[/quote]

Would it be feasible to add README or some documentation on how to run the code locally? maybe a test environment setup or architecture doc

---

### Reply #7
**Author:** gameoftrust | 2023  
**Date:** 08-24 16:16:33 UTC | #9  

[quote="root, post:7, topic:48"]
Would it be feasible to add README or some documentation on how to run the code locally? maybe a test environment setup or architecture doc
[/quote]
It’s currently worthless because I’m redesigning it and changing a lot of parts based on both user feedback and technical tests (and I’ll publish new implementations on GitHub soon), so a documentation that I write today will be useless tomorrow.

---

### Reply #8
**Author:** gameoftrust | 2023  
**Date:** 11-07 20:59:07 UTC | #10  

https://forum.iranunchained.com/t/game-of-trust-a-web-of-trust-between-iranian-protesters-report/

---

### Reply #9
**Author:** travis | 2024  
**Date:** 08-21 15:33:38 UTC | #11  

Thank you for sharing the overview of the Game of Trust. It’s an innovative approach to secure communication and coordination among those opposing the regime.

---

