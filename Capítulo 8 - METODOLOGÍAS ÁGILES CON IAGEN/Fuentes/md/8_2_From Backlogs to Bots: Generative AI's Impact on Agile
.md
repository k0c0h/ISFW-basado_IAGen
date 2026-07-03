_Journal of Software: Evolution and Process,_ 2025; 37:e2740 1 of 5
https://doi.org/10.1002/smr.

## Journal of Software: Evolution and Process

## SPECIAL ISSUE - METHODOLOGY PAPER OPEN ACCESS

# From Backlogs to Bots: Generative AI's Impact on Agile

# Role Evolution

Philipp Diebold1,

(^1) IU International University, Erfurt, Germany | (^2) Bagilstein GmbH, Mainz, Germany
**Correspondence:** Philipp Diebold (philipp.diebold@bagilstein.de)
**Received:** 6 July 2024 | **Revised:** 7 October 2024 | **Accepted:** 18 October 2024
**Funding:** The author received no specific funding for this work.
**Keywords:** agile | agile roles | AI implications | artificial intelligence (AI) | generative AI | role evolution | scrum

## ABSTR ACT

```
This position paper investigates the transformative impact of generative artificial intelligence (GenAI) on Agile roles. Focusing
on the product owner, developer, and scrum master, we analyze how GenAI redefines traditional tasks, encouraging a shift to-
wards more strategic and creative functions. Through practical experience, we illustrate AI's role in enhancing Agile processes,
its practices and emphasize the need for Agile practitioners to integrate AI understanding. These results highlight the balance
between GenAI's efficiencies and Agile's human- centric principles, proposing research directions for AI- enriched Agile prac-
tices that promise to drive innovation and maintain the agility in a technologically progressive era.
```
## 1 | Introduction

In the evolving business world, change is not just a constant but
the currency of survival and success. Companies are navigat-
ing an environment that not only evolves but also accelerates
with each technological advance. In this race against time, busi-
nesses are forced to adapt at a rapid pace, striving for agility to
meet the shifting demands of global markets and consumer ex-
pectations [1].

The relentless speed of the business world today is largely fos-
tered by digitalization, a phenomenon that has redefined the
essence of operational strategies and organizational structures.
As digital technologies weave deeper into business operations,
they create new opportunities for growth and innovation while
simultaneously disrupting established norms and practices. The
current heart of this digital revolution is artificial intelligence
(AI) [2]. AI's potential to transform the business landscape
promises to revolutionize many workplaces. The integration of
AI—especially generative AI—into various business processes
is not only optimizing existing operations but is also creating
new paradigms for work, employment, and value creation [3].

```
With this transformative power of AI, a number of jobs will
change or evolve, with AI reshaping job profiles and their tasks.
The effects are pervasive, within every domain from manufac-
turing to services witnessing a shift in the skill sets and compe-
tencies required to thrive in the new AI workplace [4].
```
```
Project management—a discipline central for the operational-
ization and execution of business strategies—is also confronted
with this transformation. The integration of generative AI prom-
ises to change project management by providing tools that not
only enhance efficiency and accuracy but also elevate decision
making and strategic planning. AI's ability to analyze vast data-
sets in real- time allows for predictive insights, risk assessment,
and resource optimization, thereby addressing some of the most
challenging aspects of project management.
```
```
As this transformation permeates the field, it naturally extends
into the specialized domain of Agile project management. Agile,
with its emphasis on flexibility, speed, and collaboration, stands
to benefit uniquely from AI's capabilities. In Agile settings, AI
tools can support refining processes such as sprint planning,
backlog management, and team dynamics, enriching the Agile
```
This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is
properly cited.
© 2024 The Author(s). Journal of Software: Evolution and Process published by John Wiley & Sons Ltd.


2 of 5 _Journal of Software: Evolution and Process,_ 2025

values of customer collaboration and responsiveness to change.
The roles of key Agile practitioners, including scrum masters
(SMs), product owners (POs), and developers, are thus evolving.
They are moving towards a new paradigm where their individ-
ual tasks are not just redefined but also enhanced by AI, calling
for a renewed understanding of Agile principles in light of AI's
potential.

The implications of this shift are vast and complex, warranting
a deeper investigation into how AI is redefining Agile project
management. This position paper is based on long- term expe-
riences in agile development and aims to explore these implica-
tions, offering insights into the synergies and challenges at the
intersection of AI and Agile methodologies with the focus on the
common roles in an agile setup.

## 2 | Agile and AI: Background

## 2.1 | Agile: A Dual Perspective

Agile methodology encompasses two fundamental sides:
the cultural and the technical. The cultural aspect of Agile
is rooted in values and principles—still strongly influenced
from the agile manifesto [5]—that prioritize individuals and
their interactions. It focuses on collaboration, customer feed-
back, and the ability to respond to change—soft skills that are
essential for Agile teams to function effectively. These soft
skills include communication, adaptability, problem- solving,
and a strong team spirit, all of which are crucial for an Agile
mindset [6].

On the technical side, Agile is characterized by its frameworks,
methods, and underlying practices. This includes various frame-
works like e.g. the most common ones, Scrum or Kanban, which
provide structure to the Agile process. The “technical” practices
which are the smallest building blocks involve routine meetings
(such as daily stand- ups, sprint planning, reviews, and retro-
spectives), artifacts (like product backlogs and sprint backlogs),
and roles (such as SM, PO, and team members) [7]. These ele-
ments serve as the backbone of Agile processes, ensuring that
Agile teams can work in a manner that is iterative, incremental,
and continuous.

## 2.2 | AI: Maximizing Potential Through

## Skillful Use

AI is a domain of computer science that aims to create systems
capable of performing tasks that typically require human intel-
ligence. Thus, it presents a powerful set of tools that have the
potential to transform industries and workflows [3, 4]. However,
it is clear that just having access to technology like this is not
enough. It necessitates a deep understanding of AI's capabilities
and limitations, and the skill to apply it in a manner that com-
plements and enhances human effort.

One and probably the most important of the emerging chal-
lenges within AI is the field of prompt engineering. This refers
to the skillful crafting of inputs and queries to effectively com-
municate with AI systems, ensuring that the outputs generated

```
are useful, relevant, and aligned with the user's intent. Prompt
engineering does not only require technical know- how but also
creativity and insight into the workings of AI language mod-
els and machine learning algorithms  [8]. As AI becomes more
prevalent, the ability to interact with and guide AI systems
through effective prompts will be a critical skill for maximizing
their potential in various applications, including Agile project
management.
```
## 2.3 | AI and (Agile) Project Management

```
Mueller et  al. [9] shows that there is still an academic interest
in understanding AI's impact on management and managerial
practices. This shift is particularly noted in project manage-
ment, where AI applications have evolved from expert systems
aiding in decision making to more intricate roles in effort esti-
mation, cost management, and risk management among other
areas. The aspect of AI on decision making in project manage-
ment is analyzed in detail in [ 10 ].
```
```
An overview based on a survey [9] of 2314 professionals from
129 countries indicates a global acknowledgment of AI's trans-
formative impact on project management. Key areas of influence
include data collection and reporting, performance monitoring,
and project scheduling. However, the findings also reveal a sig-
nificant gap in AI training within organizations, with many
professionals possessing only a basic level of AI knowledge and
experience. Despite that, there is a marked interest among proj-
ect managers to deepen their understanding of AI, recognizing
its potential to revolutionize their field. An interesting example
is given by Dam et  al. [11] about how AI—not only generative
AI—could be used for a better planning and analysis procedure,
mainly for the role of the PO.
```
```
The survey further underscores the perceived importance of
national governments in fostering AI development through
investments in technology and education, as well as in legis-
lating and establishing guidelines to ensure ethical and secure
AI practices. This collective perspective underscores the crit-
ical role of governmental intervention in facilitating the inte-
gration of AI within project management and in addressing
the broader challenges associated with AI adoption in profes-
sional settings.
```
## 3 | The Transformation of Agile Roles Through AI

```
The convergence of Agile and AI began when technologists
started recognizing AI's potential to enhance Agile processes.
AI's ability to analyze large datasets, automate routine tasks,
and provide predictive insights presented opportunities to re-
think jobs and tasks to be done in different roles [ 12 ]. Thus, the
following section is going to discuss AI's role in the current and
next evolution of agile roles—more from the viewpoint of tech-
nical agility.
```
```
Before digging into the role- specific details, it is necessary to
mention that all the following aspects perfectly fit to an agile
culture that is grounded on experimentation and adaptation.
This is the case because using GenAI technologies, especially
```

```
3 of 5
```
prompt engineering, needs an experimental culture and the user
of such tools needs to adapt [6].

## 3.1 | The Product Owner: Focus on Creativity

## and Crafting

The role of the PO is undergoing a significant transformation
influenced by the appearance of AI. The traditional focus on
product- and backlog management [ 13 ] is shifting towards a
more creative and strategic direction ( _H- PO1_ ). The PO is now
expected to engage more in crafting a product vision and strat-
egy rather than being involved in all the details of backlog items.

The product vision and its strategy rely on the PO's ability
to synthesize market trends, user needs, and business goals.
While AI can support this process by suggesting new ideas
and optimizing existing functionalities, the basic idea as well
as the responsibility for the product vision remains with the
PO. This ensures that the product aligns with the complex
combination of user needs, market demands, and ethical con-
siderations that AI alone cannot navigate. The collaboration
between the PO and AI systems necessitates a delicate bal-
ance. AI can handle vast amounts of information, but the PO
must guide it by providing the correct and relevant informa-
tion ( _H- PO2_ ). This symbiosis ensures that AI complements the
human intelligence of the PO, leading to more innovative and
strategically aligned product development.

Furthermore, the classical PO works a lot in the field of re-
quirements engineering—a task traditionally requiring ex-
tensive writing of user stories, designing user interfaces, and
outlining acceptance criteria. Generative AI has the potential
to revolutionize this facet of the PO's work by automating the
creation of text, user interfaces, even user journey maps or
other requirements- related content [11, 13]. This will allow
the PO to allocate more time to high- level strategic tasks men-
tioned before. AI systems, with its proficiency in managing
and analyzing large datasets, could take on the role of the pri-
mary backlog item creator and manager. This shift can sig-
nificantly reduce the administrative burden on the PO, who
would then refine the AI- generated backlog to ensure align-
ment with the product vision.

## 3.2 | The Dev- Team: From Code to Collaboration

The role of the software developer is being redefined most of
all the roles. AI and its capabilities increase the automation of
routine tasks ( _H- DEV1_ ), which are especially programming
and quality assurance that includes all kind of testing activities.
Furthermore, [14] showed that especially in programming, over-
all AI systems work well without many mistakes. Nevertheless,
this automation depends on providing precise inputs reflecting
the problem or need—this is where prompt engineering be-
comes important. It necessitates a deeper collaboration between
developers and PO to ensure that AI solutions are furnished
with high- quality requirements ( _H- DEV2_ ). These requirements,
effectively crafted, serve as sophisticated prompts that enable AI
to generate code, thus fostering a more integrated approach with
product development.

```
The consequence of this shift is twofold: On the one hand, it re-
leases developers from the aspect of repetitive coding tasks and
engage them in more inventive and cooperative facets of software
development. On the other hand, it repositions developers at the
leading edge of innovative problem- solving. Their expertise ex-
ceeds coding skills: All developers need to become architects of
complex software solutions ( H- DEV3 ), blending creativity with
technical proficiency. This paradigm shift is transformative,
signaling a departure from traditional programming roles to-
wards a future where developers get technical innovation lead-
ers. Their role evolves to encompass the conceptualization and
execution of advanced software solutions that are responsive to
dynamic market needs and technological possibilities.
```
## 3.3 | The Scrum Master: New Dimensions

## of Leadership

```
The Scrum Master (SM) role is often misunderstood in practi-
cal context, sometimes conflated with administrative positions
such as a scribe, secretary, or tool administrator for handling
JIRA or similar tools. Even if this is a misinterpretation, the rise
of AI offers a compelling solution to this: Certain tasks, such as
transcription or administrative tool maintenance, can be man-
aged by AI without the need for sophisticated prompting or deep
knowledge ( H- SM1 ). This allows the SM to fully embody the real
key stances: servant leader, facilitator, coach, manager, mentor,
teacher, impediment remover, and change agent [ 15 ].
```
```
AI's capacity to assume routine management tasks creates space
for the SM to move towards either a more strategic function from
management aspect or focus more on the other stances [ 15 ].
Furthermore, AI can support teaching and training through the
delivery of educational content either completely by an AI system
or in combination with a human trainer ( H- SM2a ). Independent
of the concrete training implementation, it should be followed
by continuous coaching support by the agile coaching stance ( H-
SM2b ). In facilitation, AI can enhance the creativity of meetings
such as by generating novel questions for daily stand- ups or ex-
tending existing SM tools like the Retromat for retrospectives
[16]. To give another example, with the use of generative AI, it is
easy and fast to generate topic specific meetings.
```
```
The usage of AI complements human expertise and thus is en-
suring that the SM can focus on fostering an agile culture with
continuous improvement ( H- SM3 ). This represents a significant
shift in the SM's function, moving towards a more coaching-
centric approach, aligning closely with the role of an Agile
coach. With this AI- support, the SM can redefine his focus on
the less AI- supported stances, particularly in nurturing the
team's growth, facilitating empowerment, and driving change,
thereby enhancing the agility and effectiveness of the team.
```
## 3.4 | The Agile Coach: Towards an AI- Trainer

```
With the SM going more into a coaching role, this follows the
same direction with the Agile coaching role. Similar to this, the
coach focuses more on the human aspects than the knowledge
and consulting aspects, such as methodologies. Therefore, they
focus on nurturing soft skills and interpersonal dynamics that
```

4 of 5 _Journal of Software: Evolution and Process,_ 2025

facilitate high- functioning teams ( _H- AC1_ ). As a change agent,
the Agile coach is becoming increasingly critical, serving not
just to inspire change and coming up with a methodological tar-
get or vision, but taking people along.

The role of a coach in general is at the intersection of intent
and action, where they work to close the gap between the
ideation of practices and their execution [17]. So, the Agile
coaches' idea is to coach a group of people or team towards an
agile mindset, most often by adapting behaviors and processes
together with them.

Coming back to some methodology aspect that was mentioned
before, the Agile coach can leverage AI to enhance the creation
and refinement of organizational structures towards an Agile
environment ( _H- AC2)_. However, this requires precise context—
again highlighting the importance of skills such as require-
ments engineering and prompt engineering—to ensure that AI
tools are effectively used and come up with the solutions or ideas
tailored to the organization's needs ( _H- AC2_ ).

The modern Agile coach must combine traditional coaching
techniques, method knowledge on agility with a profound un-
derstanding of AI's capabilities. This expertise allows them
to guide teams not only in adopting Agile principles and
practices but also in integrating AI into their workflows. By
doing so, they enable other roles—such as the PO, developer,
and SM—to adapt to their evolving responsibilities in an AI-
augmented workplace.

In sum, the Agile coach is key to helping teams navigate the
complexities of change, encouraging a culture of continuous
improvement, and ensuring that the human aspects of Agile
are amplified in the face of technological advancements. They
act as a bridge between human intuition and AI's analytical
prowess, fostering an environment where both can thrive in
s y nerg y.

## 4 | Discussion

The integration of AI into Agile roles represents a paradigm
shift in project management and software development—as
in many other domains as well. Our examination of the trans-
formed tasks of POs, developers, and SMs has brought up sev-
eral hypotheses to the mentioned roles working with generative
AI (see Table 1).

Besides these role- specific hypothesis, by highlighting the po-
tential of AI to enhance efficiency and innovation, we need to
present challenges that necessitate a reevaluation of traditional
Agile practices.

## 4.1 | Synergy and Redefinition of Roles

AI's role in Agile practices is not merely functional but trans-
formative, fostering a deeper synergy between technological
possibilities and human expertise. POs are now able to tran-
scend the operational focus on backlog management, leverag-
ing AI to contribute more strategically and creatively to product

```
vision. Developers are shifting from routine coding to complex
problem- solving, with AI automating the mundane and freeing
human intelligence for higher- order functions. For SMs, AI of-
fers support in administrative tasks, allowing them to focus on
the coaching and facilitative aspects of their role, thus becoming
more integral in guiding Agile transformations.
```
## 4.2 | Ethical and Practical Considerations

```
Although AI's potential to assume certain tasks within Agile
roles is evident, ethical and practical considerations emerge.
Dependence on AI for tasks such as backlog management and re-
quirements engineering raises questions about the loss of human
judgment in critical decision- making processes [10, 18]. There is a
need for a guideline or framework that ensures AI tools are used
responsibly—similar to [19] and that the core Agile values of indi-
vidual and interactions over processes and tools are maintained.
```
## 4.3 | The Future of Agile Coaching

```
The evolving role of the Agile Coach is particularly noteworthy.
As the purveyor of the Agile mindset, the Agile Coach's role
becomes even more crucial in an AI- driven environment. They
must now navigate the intricacies of human- AI collaboration,
```
```
TABLE 1 | Summary of all hypothesis.
```
```
ID and role Hypothesis
```
```
H- PO1 The product owner focuses on
creative and strategic activities
instead of management.
```
```
H- PO2 The product owner guides GenAI
tools by providing the correct
and relevant information.
```
```
H- DEV1 The developers increase the automation
of routine tasks with GenAI tools.
```
```
H- DEV2 The developers strongly collaborate with
the PO to create high- quality input for AI
tools—also with the usage of AI tools.
```
```
H- DEV3 Each developer becomes a (software)
architect of complex software solutions.
```
```
H- SM1 The scrum master increases the
automation of administrative
tasks with GenAI tools.
```
```
H- SM2 The scrum master focuses on practical
coaching and increases teaching
and training with AI tools.
```
```
H- SM3 The scrum master focuses on
fostering an agile culture with
continuous improvement
```
```
H- AC1 The Agile coach focuses on development
of soft skills and interpersonal dynamics.
```
```
H- AC2 The Agile coach fosters the usage of AI
tools and ensures an effective usage.
```

```
5 of 5
```
ensuring that AI tools are employed in ways that enhance rather
than undermine human and team dynamics.

## 5 | Conclusions

This position paper has embarked on a comprehensive explo-
ration of the transformative influence of AI on Agile roles. We
have observed the paradigm shift from routine, task- oriented
functions towards strategic, creative, and complex problem-
solving activities. The PO is evolving into a visionary strategist,
the developer into an innovative problem solver, and the SM into
a facilitative leader, each enabled by AI's capacity. This change
or reshaping of the focus of the different agile roles is manifested
in 10 hypotheses of this position paper (see Section 4) that could
and should guide us in future research to be validated or not.

The insights garnered point to a future where Agile meth-
odologies and AI converge to create a dynamic, efficient, and
human- centered approach to project management. However,
this convergence does not come without challenges. It necessi-
tates a vigilant reassessment of Agile's core values and princi-
ples, ensuring they remain at the forefront amidst the drive for
technological efficiency.

As Agile roles adapt to incorporate AI, there is an imperative
need for the Agile community to foster an environment where
technology acts as a complement to human expertise, not a
substitute. This balance is crucial in maintaining the essence
of Agile—its emphasis on people, interactions, and customer
collaboration. The Agile community must continue to embrace
change, as it always has, but with a renewed focus on ensuring
that the technology serves to augment the human elements that
are the cornerstone of Agile success.

**Acknowledgements**

Open Access funding enabled and organized by Projekt DEAL.

**Data Availability Statement**

Data sharing not applicazble to this article as no datasets were gener-
ated or analysed during the current study.

**References**

1. B. Boehm and R. Turner, “Observations on Balancing Discipline and
Agility,” in _Proceedings of the Agile Development Conference, 2003. ADC
2003_ (Salt Lake City, UT: IEEE Computer Society, 2003): 32–39.
2. R. Dornberger, T. Inglese, S. Korkut, and V. J. Zhong, “Digitalization:
Yesterday, today and tomorrow,” _Business Information Systems and
Technology 4.0: New Trends in the Age of Digital Change_ , 1–11 (2018)
3. C. Davies, “Precarious Work & The Digital Economy: Next Phase of a
New Work Paradigm,” (2022)
4. V. Pereira, E. Hadjielias, M. Christofi, and D. Vrontis, “A Systematic
Literature Review on the Impact of Artificial Intelligence on Workplace
Outcomes: A Multi- Process Perspective,” _Human Resource Management
Review_ 33, no. 1 (2023): 100857.
5. K. Beck, M. Beedle, A. Van Bennekum, et al., “The Agile Manifesto,”
(2 0 01)
    6. T. Kuchel, M. Neumann, P. Diebold, and E. M. Schön “Which
    Challenges Do Exist With Agile Culture in Practice?,” In _Proceedings_
    _of the 38th ACM/SIGAPP Symposium on Applied Computing_ (2 023):
    1018–1025.
    7. K. Schwaber and J. Sutherland, “The Scrum Guide,” _Scrum Alliance_
    21, no. 1 (2011): 1–38.
    8. J. D. Velásquez- Henao, C. J. Franco- Cardona, and L. Cadavid-
    Higuita, “Prompt Engineering: A Methodology for Optimizing Interac-
    tions With AI- Language Models in the Field of Engineering,” _Dynamis_
    90, no. 230 (2023): 9–17.
    9. R. Müller, G. Locatelli, V. Holzmann, M. Nilsson, and T. Sagay, “Arti-
    ficial Intelligence and Project Management: Empirical Overview, State
    of the Art, and Guidelines for Future Research,” _Project Management_
    _Journal_ 55, no. 1 (2024): 9–15.
    10. M. El Khatib and A. Al Falasi, “Effects of Artificial Intelligence on
    Decision Making in Project Management,” _American Journal of Indus-_
    _trial and Business Management_ 11, no. 3 (2021): 251–260.
    11. H. K. Dam, T. Tran, J. Grundy, A. Ghose, and Y. Kamei, “Towards
    Effective AI- Powered Agile Project Management,” in _2019 IEEE/ACM_
    _41st International Conference on Software Engineering: New Ideas and_
    _Emerging Results (ICSE- NIER)_ (Montreal, QC, Canada: IEEE, 2019,
    May), 41– 4 4.
    12. L. Ayinde and H. Kirkwood, “Rethinking the Roles and Skills of
    Information Professionals in the 4th Industrial Revolution,” _Business_
    _Information Review_ 37, no. 4 (2020): 142–153.
    13. R. Pichler, _Agile Product Management With Scrum: Creating Prod-_
    _ucts That Customers Love_ (Boston, MA: Addison- Wesley Professional,
    2010).
    14. J. R. Koza, M. A. Keane, and M. J. Streeter, “What's AI Done for me
    Lately? Genetic Programming's Human- Competitive Results,” _IEEE In-_
    _telligent Systems_ 18, no. 3 (2003): 25–31.
    15. B. Overeem “The 8 Stances of a Scrum Master,” _URL:_ ht t p s : //
    scrumorg- website- prod.s3.amazonaws.com/drupal/2017- 05/The, _208_
    (2 017)
    16. C. Baldauf, _Retromat- Run Great Agile Retrospectives_ (Layton: Lean-
    pub, 2018).
    17. C. C. Schermuly and C. Graßmann, “A Literature Review on Nega-
    tive Effects of Coaching–What We Know and What We Need to Know,”
    _Coaching: An International Journal of Theory, Research and Practice_ 12,
    no. 1 (2019): 39–66.
    18. K. Siau and W. Wang, “Artificial Intelligence (AI) Ethics: Ethics of
    AI and Ethical AI,” _Journal of Database Management (JDM)_ 31, no. 2
    (2020): 74–87.
    19. Q. Lu, L. Zhu, X. Xu, J. Whittle, D. Zowghi, and A. Jacquet, _Re-_
    _sponsible ai Pattern Catalogue: A Collection of Best Practices for ai_
    _Governance and Engineering_ (New York, NY: ACM Computing Sur-
    veys, 2 023).


