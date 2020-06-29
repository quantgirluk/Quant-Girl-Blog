# The Quant Project

After finishing my studies at the University of Warwick I decided to become a Quantitative Analyst (a.k.a. a Quant). So, I started looking for jobs in the Financial sector. I applied for lots of positions and attended lots of interviews. The hardest part of this process was not knowing exactly what to expect or how to prepare for the interviews. This is why I want to share some insight with students who may find themselves in a similar position.

This post will cover:

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Types of Quant](#types-of-quant)
- [:school: Skills](#school-skills)
	- [Maths and Statistics](#maths-and-statistics)
	- [Programming - Computer Science](#programming-computer-science)
	- [Others](#others)
	- [Soft Skills](#soft-skills)
- [Interview Process](#interview-process)
	- [📓Resume](#resume)
	- [:dart: General Tips](#dart-general-tips)
	- [:telephone: Telephone Round](#telephone-telephone-round)
	- [:busts_in_silhouette:  Face to Face Rounds](#bustsinsilhouette-face-to-face-rounds)
- [Resources](#resources)
	- [:books: Books](#books-books)
	- [:globe_with_meridians: Free Online Resources](#globewithmeridians-free-online-resources)
	- [:desktop_computer: Coding Practice](#desktopcomputer-coding-practice)
	- [:busts_in_silhouette: Recruiters](#bustsinsilhouette-recruiters)
- [:question: FAQs](#question-faqs)

<!-- /TOC -->

---
## Types of Quant

As you may know there are many types of Quants and they do different things and  require different skill sets.

### By Department

- Front Office/Desk Quants/Algorithmic Trading

Implement pricing models, analytics, and algorithms directly used for trading (either by traditional traders or algo-traders) and sales.

These quants develop models to work out the prices of assets on the markets and manage them: what to buy at and what to sell at etc. The calculations they make also help to provide guidance on risk management and support the traders in the development of their risk strategies. They are also busy on the investment/business development side of things, using their mathematical and statistical techniques to spot potential new investment opportunities.

- Risk Management

Risk quants belong to the middle office. Quants in this area produce analytics on the different kinds of risk (market, counterparty, wholesale etc.) and communicate their findings to risk managers. They also own the regulatory capital calculations and internal risk management measures.

- Model Validation

Independently review and implement pricing/risk models in order to assess their soundness and quantify its limitations.

### By Activity

- Researcher

As the name indicates, the job involves conducting research to solve problems that arise within the bank (e.g. creating  pricing models for new products, improving simulation models, developing new trading algorithms, etc.) These are the most suitable positions for those who love mathematics. It is also an ideal way to get a smooth transition from academia to finance.

These jobs usually require a basic to medium level of coding.

- Developer

Again, as the name indicates this kind of job involves implementation. This includes, implementation and maintaining of models (sometimes developed by other people), process automation (e.g. move a process from 100 spreadsheets to a web application).

Unsurprisingly, these jobs usually require a medium to high level of coding.


---
## :school: Skills

Hard Skills to become a quant can be classified in three areas: **Maths, Statistics, and Programming**. Next is a list of concepts that would give you a good foundation for the interviews. This list is (of course) not exhaustive but if you are familiar with all these concepts, you will be in a good path to pass your interviews.


Please keep in mind that you don't need to be an expert on everything. Having some knowledge on the basics of each topic is enough to start your career. Once you start in your new position you can focus on strengthening the areas that you use the most on your everyday activities.

Besides, every interview will focus on different aspects of these areas depending on the requirements of the job. This is why it is very important to **read carefully the job description** and **tailor your preparation** accordingly.


### Maths and Statistics

- Probability Theory and Statistics
  - Basic Distributions (Normal, Log-Normal, t-Student, Bernoulli, Binomial, Exponential, Poisson, etc.)
  - Basic Probability Concepts such as Expectation, Variance, Quantiles (for some reason that I still don't understand people in banks prefer to call them percentiles),  CDF, PDF, etc.
  - [Law of Large Numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers)
  - [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)


- Algebra
  - [Matrix Decompositions](https://en.wikipedia.org/wiki/Matrix_decomposition)
    - [Cholesky](https://en.wikipedia.org/wiki/Cholesky_decomposition)
    - [Spectral](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix)

  - Principal Component Analysis [(PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis)


- Stochastic Processes
  - [Brownian Motion](https://en.wikipedia.org/wiki/Brownian_motion)/[Wiener Process](https://en.wikipedia.org/wiki/Wiener_process)
  - [Geometric Brownian Motion](https://en.wikipedia.org/wiki/Geometric_Brownian_motion) Solving the GBM equation is a very common question for junior quants interviews.
  - [Orstein-Ulehbeck](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process)
  - [Martingale](https://en.wikipedia.org/wiki/Martingale_(probability_theory))
  - [Ito's Formula](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma) (Mainly to calculate expectations and solve SDEs)
  - [Black-Scholes Model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) in terms of SDEs
  - [Girsanov Theorem](https://en.wikipedia.org/wiki/Girsanov_theorem) Most likely you will need to use this result for a Change of [numéraire](https://en.wikipedia.org/wiki/Num%C3%A9raire).
  - [Forward Measure](https://en.wikipedia.org/wiki/Forward_measure) (also called T-measure)



- PDEs
  - [Black-Scholes Model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) in terms of PDEs.


- Statistics
  - [Linear](https://en.wikipedia.org/wiki/Linear_regression) and [Logistic](https://en.wikipedia.org/wiki/Logistic_regression) Regression
  - [Generalised Linear Models](https://en.wikipedia.org/wiki/Generalized_linear_model)
  - [Lasso Regression](https://en.wikipedia.org/wiki/Lasso_(statistics))
  - [Hypothesis Testing](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing) Be ready to explain [Type I and Type II](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors) error.
  - [Confidence Intervals](https://en.wikipedia.org/wiki/Confidence_interval)
  - [Bootstraping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) Methods
  - Maximum Likelihood Estimation [MLE](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)


- Time Series - For a quick summary I recommend this [Introduction to the Fundamentals of Time Series Data and Analysis
](https://www.aptech.com/blog/introduction-to-the-fundamentals-of-time-series-data-and-analysis/)
  - Basic concepts as trend, seasonality, stationarity,
  - Autoregressive Moving Average Models [ARMA](https://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model)
  - Autoregressive Integrated Moving Average Models [ARIMA](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average)
  - Vector Autoregressive Models [VAR](https://en.wikipedia.org/wiki/Vector_autoregression)
  - Autoregressive Conditional Heteroscedasticity [ARCH](https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity) and Generalised Autoregressive Conditional Heteroscedasticity [GARCH](https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity#GARCH) models.



- Bayesian Statistics (This one is becoming trendy!)
  - [Bayes' Rule](https://en.wikipedia.org/wiki/Bayes%27_theorem)
  - [Pior probability](https://en.wikipedia.org/wiki/Prior_probability)
  - [Posterior probability](https://en.wikipedia.org/wiki/Posterior_probability)



- Numerical Methods
  - [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method)
  - Optimisation Methods
      - [Nelder-Mead](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method),
      - [Newton](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)
      - [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent)
  - [Finite Differences Method](https://en.wikipedia.org/wiki/Finite_difference_method)


### Programming

The level of programming skills will depend on the kind of job. Broadly speaking junior roles (immediately after uni or less than 2-3 years experience) will require a basic to medium level of programming. Programming languages vary among banks but I would say Python and C++ are the most popular in the industry.

- Python and R are typically used to prototype models, perform data analysis, testing alternative models, etc.

- C++ or Java are typically used for production libraries.

- [Sorting Algorithms](https://www.geeksforgeeks.org/sorting-algorithms/)  are very popular in the quant interviews.
- Complexity of different algorithms. For this purpose, I seriously recommend you to take a look at the [Big O Cheat Sheet](https://www.bigocheatsheet.com/) 😃

### Other Tools

- Data Basis
  - SQL
- Scientific Writing
  - [Latex](https://www.latex-project.org/about/) - I am happy to report that most quant teams have adopted Latex to write their documentation. Thus, your experience with Latex will become very useful :sunglasses:
  - [Markdown](https://www.markdownguide.org/getting-started/)

- Version Control. Get familiar with some kind of version control documentation, for instance:
    - [Perforce](https://en.wikipedia.org/wiki/Perforce) (p4)
    - [Git](https://git-scm.com/), [GitHub](https://github.com/)

- Office - Yes, I know this sounds a little bit outdated but I have to say that Excel, Word, and PowerPoint are still very well regarded within banking.


### Soft Skills

In addition to all the technical knowledge, you will need to cultivate your _Soft Skills_. These are by no means less important than hard skills!

In fact, I have seen many examples where they play a key role in an interview process. Why? because Quants generally don't work alone. You will be part of a team and will spend many hours discussing and sharing ideas with them.


In every interview, the interviewers want to answer two important questions:

- Can this person do the job?
- Can I work with this person?

The first question will be covered by the technical part of the interview. The second one is more difficult. Here are some important soft skills that you can focus on ahead of an interview:

- Communication

Tip: Prepare a 5 minutes summary of your PhD/MSc thesis.
In many interviews I have been asked to explain my PhD thesis in simple terms. I know that every PhD can talk for hours and hours about his/her dissertation... however the key here is in the last bit **simple terms**. Try to prepare a 10 minutes summary of your PhD avoiding too technical terms (this is particularly challenging for theoretical mathematicians but it is worth the effort). Then try to cut it in half the time by making it briefer.

- Collaboration

As I mentioned, you won't work alone. Projects in the industry are so big that is difficult (or impossible) for one person to do everything. Thus, you have to learn to work efficiently as a member of a team.


- Adaptability

Banking as most of the industries nowadays is changing constantly and at a rapid pace. So you need to be able to

---

## Interview Process

### 📓Resume

Before sending your applications, take some time to update your resume and LinkedIn profile.

Get ready to answer the most common question: **Walk me through your resume**. Practice at home by trying to describe your academic background and experience in 5 to 10 minutes. The idea is to introduce yourself and give the interviewer a broad idea of your experiences and how they are relevant for the job. This question usually aims to open the conversation so you maybe interrupted and asked to elaborate on certain points.

Besides, be prepared for explaining your resume in **full**. This means, making sure that you know **every single word** written on it. If you don't know it well, don't write it on your resume. Your interviewer expects you to be able to explain all the things written there.

### :dart: General Tips


⭐**Online Presence**⭐ Keep in mind that your interviewer(s) will (almost surely) make a quick Google search with your name on it. So be mindful about your online image. Use your online presence to display your skills ⭐

  - GitHub
  - Personal Website
  - RPubs collection
  - Kaggle profile



⭐**Continuous Learning**⭐ Include all your (MOOCs) Massive Open Online Courses certifications in your resume. It shows that you are motivated,  committed to your development, and can learn new stuff independently. So, don't forget all those Coursera, DataCamp, Udemy, Pluralsight, etc. certifications.


⭐**Keep it Real**⭐ Be honest when you don't know. This is much better than inventing something. Nobody knows everything and the people who are interviewing you know that. So please, don't be scared to ask for hints or suggestions. I have seen many candidates who are struggling with a question but just need a small hint and then they figure out the rest pretty quickly! This looks great because  it shows that you can deal with difficult situations, ask for help, use that help to get a positive outcome!

⭐**Show Interest**⭐ Ask Questions about the team, what it does? how is the structure (is it a big or small team, are you being hired for a particular project, for a backfill, or for a team expansion)

### :telephone: Telephone Round

Almost all recruitment processes include an initial telephone interview. This is usually less formal (which does not imply less technical) than the face to face (teleconference) round. The idea is to get to know the candidate.

- Find a quiet place to have the interview and make sure that you have good reception
- Print your resume and have it with you (or at least have it on the screen)

### :busts_in_silhouette:  Face to Face Rounds

Then there are several face to face (or teleconference) interviews. Here you will meet more members of the team and the questions will be more technical. In my experience you may have between 2 and 7 of these in a day (so have a good breakfast before going into one of those super days!).

- Be on time and wearing professional clothes
- Don't be nervous, these are just people like you and me. I know that as a recent graduate the first interviews can be intimidating. But please be confident and keep in mind that being invited for this round means a high change of success! You are already in the short list of candidates who passed.
- Bring printed copies of your resume, as well as bank paper and pens to write.
- Listen carefully to each question and make sure you understood it. If you are not sure, ask questions.
- Show interest on the role and the team.
- Ask for the next stages of the hiring process.

---
## Resources

### :books: Books

These are some of the most popular **books** for preparation. I bought all of them back in 2016 when I started interviewing with banks. All of them are good (and of course there is some intersection of the questions among them) but I would focus on the first two.


- Quant Interview Questions and Answers by Mark Joshi [Amazon Link](https://www.amazon.co.uk/Quant-Interview-Questions-Answers-Second/dp/0987122827/ref=sr_1_1?crid=3NMWONSVPN3V7&dchild=1&keywords=quant+interview&qid=1589298474&sprefix=quant+inter%2Caps%2C147&sr=8-1)

- Frequently Asked Questions in Quantitative Finance [Amazon Link](https://www.amazon.co.uk/Frequently-Asked-Questions-Quantitative-Finance/dp/0470748753/ref=pd_sbs_14_7?_encoding=UTF8&pd_rd_i=0470748753&pd_rd_r=dfa6d009-d708-427b-9cde-171f33d1fcbf&pd_rd_w=3xDhg&pd_rd_wg=iUX0m&pf_rd_p=2773aa8e-42c5-4dbe-bda8-5cdf226aa078&pf_rd_r=96G2QQM96135K78BFEFV&psc=1&refRID=96G2QQM96135K78BFEFV)


- Heard on The Street: Quantitative Questions from Wall Street Job Interviews [Amazon Link](https://www.amazon.co.uk/Heard-Street-Quantitative-Questions-Interviews/dp/0994138695/ref=pd_bxgy_3/262-8107884-6043037?_encoding=UTF8&pd_rd_i=0994138695&pd_rd_r=2d4c8b18-5505-4193-b9ff-ffe9f2829825&pd_rd_w=r4dxL&pd_rd_wg=1X4PH&pf_rd_p=106f838b-b7d1-46e9-83e0-f70facc857bf&pf_rd_r=J3FHSFP551P3AECXN86V&psc=1&refRID=J3FHSFP551P3AECXN86V)

- A Practical Guide To Quantitative Finance Interviews [Amazon Link](https://www.amazon.co.uk/Practical-Guide-Quantitative-Finance-Interviews/dp/1438236662/ref=pd_bxgy_img_2/262-8107884-6043037?_encoding=UTF8&pd_rd_i=1438236662&pd_rd_r=bff93f8d-1933-43da-97db-00553285597f&pd_rd_w=rQA36&pd_rd_wg=C9lGh&pf_rd_p=106f838b-b7d1-46e9-83e0-f70facc857bf&pf_rd_r=GSXDQP7B2E50BSZ80331&psc=1&refRID=GSXDQP7B2E50BSZ80331)


### :globe_with_meridians: Free Online Resources

- [Brainstellar](http://brainstellar.com/) for math puzzles
- [Quantopian Lectures](https://www.quantopian.com/lectures) great collection of Python Notebooks explaining basic concepts in finance. You can clone the notebooks and reproduce the results. It is a great way to review your basic maths and practice Python at the same time.
- [Quantpedia](https://quantpedia.com/) They describe themselves as "The Encyclopedia of Algorithmic and Quantitative Trading Strategies". You can browse around 70 strategies for free.
- [QuantStart](https://www.quantstart.com/) Focus on Algorithmic trading  techniques.

🐍Python Specific

- [Top 40 Python Interview Questions & Answers](https://www.guru99.com/python-interview-questions-answers.html) by guru99.
- [100 Essential Python Interview Questions (Edition 2019)](https://www.techbeamers.com/python-interview-questions-programmers/) by TechBeamers
- [50 Python Interview Questions and Answers](https://dev.to/educative/50-python-interview-questions-and-answers-nh2) by Dev.to


### :desktop_computer: Coding Practice
For learning and practicing coding, I recommend

- [educative Blog](https://www.educative.io/blog)
- [Data Camp](https://learn.datacamp.com/courses)
- [Pluralsight](https://app.pluralsight.com/library/free)
- [Pythorch Tutorials](https://pytorch.org/tutorials/)


### :busts_in_silhouette: Recruiters

Finally, I want to talk a little bit about recruiters. In my experience, having a recruiter can have a huge positive impact on your job search.

- They know the market and have tons of experience with Quant interviews. They can help you to identify your strengths and find jobs that are more in line with them.

- They know people in all the banks and can give you insights on what is happening. They may know if a team is growing (which probably means that they have exciting projects coming... or lots of people leaving) or if a team is looking for juniors rather than experienced candidates.

- They really want to help you to get a job (that is what they do for a living :)) So, even if there is no positions at the moment, they will keep a copy of your resume and may call you later when something new comes up.
- They can help you to negotiate your salary. As a junior (especially as a recent PhD graduate) negotiating a compensation package can be intimidating. Discussing your salary expectations with your recruiter can help you in two ways: (1) it will give you an idea of the salary benchmarks for someone your profile; (2) it can give you confidence to talk about these topics.

- Speaking with recruiters can be useful to get familiar with long telephone conversations. They talk to people every single day and are very confident (you can learn from them!)
- They are part of the business. You will establish long lasting relationships and every time that you want to take a look at the market you will know who to contact ;)

You may be wondering how to find a recruiter. See the FAQs below.

---

## :question: FAQs


##### Can I become a quant if I have no experience in banking?
Yes, absolutely. I did not have any experience (no summer placement, no internships).

#####  How to find a recruiter?

The truth is that they may find you first. That is what they do. When I was still at Warwick recruiters started calling me and sending me messages about opportunities.

In case they have not find you yet, there are a couple of things that you can do to find them:

- Ask people in your network to recommend you a recruiter.
- Go to LinkedIn and try to find them either by finding connections or by applying to jobs (when you apply for a job via LinkedIn there is an option to let the person who post it to see your profile).
- Attend Career Fairs and Networking events
- Upload your resume to sites such as [e-finalcial careers](https://www.efinancialcareers.co.uk/)


As I mentioned, my experience with recruiters have been terrific so far. However, not all recruiters are the same. Some are amazing and others not so much. Only experience will tell you who to keep in contact with but a general rule is to look for someone who listen to you and try to understand what you are looking for (or even more, helps you to understand what are the options and to find what is more suitable for your profile and preferences). Finally, don't let recruiters push you to apply for positions that you don't like. It will be a waste of time for both most likely.



#####  How do you overcome nervousness in an interview?

Be confident in your technical skills and remind yourself that nobody knows everything. Moreover, as a recent graduate you will bring novelty and fresh air to the industry! So, please keep in mind that you have something very valuable to offer to the team.

#####  What does your typical day look like?

As a risk management quant a typical day consists of
- reading and replying to e-mails
- working on my main projects (I usually have several short term projects and one or two long term ones.) This can include: reading and writing technical documentation (mainly documents in latex) about mathematical models; writing scripts (mostly in Python at the moment) or running scripts (written by me or by others) to get some analysis done; meeting colleagues for discussing results; preparing slides for internal and external meetings.
- attending various meetings for administrative purposes such as planning, prioritising, and organising future work;


#####  Do I need a certification (e.g. CFA, FRM or CQF)?

Not really but it can help you to differentiate yourself from other candidates.

##### What has been the hardest part of transitioning to Finance?
Here are the 3 harder things from my transition from PhD student to Quantitative analyst:

**1. Missing Academia.** In baking, especially as a junior, you will have to do some tasks which are not particularly challenging from an intellectual point of view.  For example, cleaning data, copy-paste tasks, updating spreadsheets, organising files, etc. This is totally normal and part of the learning experience. But in those moments you cannot help but miss academia (the old good days when you were doing frontier research with your supervisor). However, you have to be patient and don't stress too much about it. I can guarantee that there are plenty of interesting areas and problems waiting to be solved in the industry.

**2. The noise in the office.**  As a student I was used to work on a very quiet environment (either sharing an office with other graduate students or at home on my own). So, when I went to banking the noise was a shock to me. So many people sitting on an open space having telephone conversations or video-conferences at the same time. I remember thinking how can these people focus and read a technical document in the middle of this chaos? ... After a couple of months I got used to it (and of course now I am also one of the people constantly over the phone ☎️😏 probably annoying new comers!). Top secret (not so secret) I got a pair of noise cancelling headphones 🎧😄

**3. Change happens slowly in big corporations.** As a PhD student you have all the freedom and control on your projects, priorities, and timelines. In a big company you will be part of a team (which is in turn part of a bigger team, division or department) with a hierarchical structure, where things work on a certain way and you won't have as much freedom and control on the decision making process. So, you may encounter that improving/changing something (a methodology, a process, a way of doing things) can be a slow and hard process. But you have to learn and adapt to the new rhythm. There are things in banking that move super fast but others not so much and you have to learn to be persistent and patient at the same time. If you have an idea :bulb:  that you  think can help the team to do things better ⭐, share it with your manager, push for it, try to make it happen. Don't be discouraged if it cannot be implemented immediately. Sometimes change takes time.

##### What has been the most enjoyable part of transitioning to Finance?

**1. Growing Horizontally.**  As a graduate student I spend years deepening my knowledge on a small area of mathematics. When I moved to banking I started expanding my knowledge horizontally. This is possible because there is a great variety of projects that you can work on. I started working on credit scorecards

**2. Working on a multidisciplinary team.** I have been fortunate to work along  colleagues with academic background in Computer Science, Physics, Chemistry, Economics, Business, Pure Maths (Topology, Algebra, Number Theory). Working on a multidisciplinary team has been an enriching and amazing experience.


**3. The Market is very Exciting.**  You cannot get bored in banking. There is always something happening in the markets. From regulatory changes and political turmoil to interest rates cuts and tax wars among countries. This constant change brings new challenges and opportunities.

##### Do you need a PhD to become a quant?

No, you don't need a PhD but if you have one, then you have already acquired a bunch of transferrable skills that will be super valuable in finance.

Many MSc' students have asked me if they should do a PhD before starting a career as a quant. My advise is, don't do a PhD for any other reason than pure intellectual curiosity. If you are passionate about science and want to spend 3-4 years doing research on a particular subject, go for it! But don't do it thinking of helping your future career (as a quant or anything else). You can have a brilliant career with or without a PhD (there are plenty of examples of both cases).

In my opinion, the key is being passionate about what you are doing. Once you start working as a quant, you will learn (all what you need to do your job) by doing instead of studying.


##### Some further thoughts on the PhD element

Transitioning from Academia into Finance can be a hard decision. But you can be sure that PhD are very welcome in Finance. Don't be afraid and please remember that you have acquired lots of transferrable skills. At the end of the day, working as a quant means solving difficult problems using mathematical tools and you have experience with this. Here is a short list of the skills that I learned during my PhD and have been useful in the industry.

- Solving problems using a scientific approach
- Look at the Big-Picture
- Get to know the Literature
- Break the problem into small ones
- Managing your Time
- Working under Pressure
- Writing technical documents
- Presenting your work to others


---
