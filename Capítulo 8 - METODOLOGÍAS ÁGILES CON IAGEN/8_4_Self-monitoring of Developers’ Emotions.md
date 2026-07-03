# Self-monitoring of Developers’ Emotions: The Case of Agile

# Retrospective Meetings

## DANIELA GRASSI, FILIPPO LANUBILE, NICOLE NOVIELLI, andLUIGI QUARANTA,

University of Bari, Bari, Italy

## ALEXANDER SEREBRENIK,Eindhoven University of Technology, Eindhoven, Netherlands

Developers experience a wide range of emotions while creating software. Being able to identify the causes
of one’s own and peers’ emotions can equip developers with the ability to regulate their behavior to restore
positive moods and productivity. In this article, we investigate to what extent self-monitoring of emotions
can enhance agile retrospective meetings by improving the emotion awareness of participants. To this aim,
we conducted a controlled experiment involving three software development teams involving two student
teams and one professional developers team. The experimental design involves the collection of biometrics
and self-reported information about emotions, which are then visualized before the retrospective meetings to
inform discussion using EmoVizPhy, a tool that we designed and implemented for this aim. While students
found that self-monitoring helped them recall significant emotional episodes, leading to more meaningful
contributions during retrospectives, professional developers perceived limited benefits from this practice.
Furthermore, based on the analysis of corrective actions identified by the participants during the study, we
hypothesize that self-monitoring of emotions through EmoVizPhy may play a valuable role in facilitating the
consolidation of new agile teams for which roles and collaboration dynamics are still being defined.

CCS Concepts: •Software and its engineering; •Human-centered computing→Collaborative and
social computing;Computer supported cooperative work;

Additional Key Words and Phrases: emotion awareness, agile teams, retrospective meetings, biometric sensors,
visualization

The research of D. Grassi is partially funded by D.M. 352/2022, Next Generation EU, PNRR, in the scope of the project
“Recognition of emotions of cognitive workers using non-invasive biometric sensors,” co-supported by Exprivia, CUP
H91I22000410007. This research was co-funded by the NRRP Initiative, Mission 4, Component 2, Investment 1.3, partnerships
extended to universities, research centers, companies, and research D.D. MUR no. 341, March 15, 2022, Next Generation EU
(Future Artificial Intelligence Research [FAIR], code PE00000013, CUP H97G22000210007), the Complementary National
Plan PNC I.1, Research initiatives for innovative technologies and pathways in the health and welfare sector, D.D. 931 of
June 6, 2022 (Digital Lifelong prevention initiative (DARE), code PNC0000002, CUP B53C22006420001), and by the European
Union, Next Generation EU through the Italian Ministry of University and Research, Projects PRIN 2022 (Continuous
Quality Improvement of AI-based Systems [QualAI], grant no. 2022B3BP5S, CUP H53D23003510006).
Authors’ Contact Information: Daniela Grassi (corresponding author), University of Bari, Bari, Italy; e-mail:daniela.
grassi@uniba.it; Filippo Lanubile, University of Bari, Bari, Italy; e-mail: filippo.lanubile@uniba.it; Nicole Novielli,
University of Bari, Bari, Italy; e-mail: nicole.novielli@uniba.it; Luigi Quaranta, University of Bari, Bari, Italy; e-mail:
luigi.quaranta@uniba.it; Alexander Serebrenik, Eindhoven University of Technology, Eindhoven, Netherlands; e-mail:
a.serebrenik@tue.nl.

This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives International
4.0.

© 2026 Copyright held by the owner/author(s).
ACM 1557-7392/2026/5-ART
https://doi.org/10.1145/


164:2 D. Grassi et al.

ACM Reference format:
Daniela Grassi, Filippo Lanubile, Nicole Novielli, Luigi Quaranta, and Alexander Serebrenik. 2026. Self-
monitoring of Developers’ Emotions: The Case of Agile Retrospective Meetings.ACM Trans. Softw. Eng.
Methodol.35, 6, Article 164 (May 2026), 38 pages.
https://doi.org/10.1145/

1 Introduction

Emotions play an important role in software development, as they can influence developers’ well-
being, productivity, and job satisfaction [11, 32, 35]. Recent studies investigated the relationship
between developers’ emotions, as they emerge during programming tasks, and their self-assessed
productivity [26]. Empirical results show that positive emotions, like happiness, can be linked to
increased productivity [35], while negative ones, like frustration and anger, can be detrimental and
are associated with the perception of being less productive [25, 63].
At an individual level, emotional self-awareness can equip developers with the ability to con-
sciously regulate their emotional experiences and expressions, e.g., by mitigating negative emotions
in favor of productivity [19]. As far as collaborative work is concerned, psychology suggests that
emotional awareness is also an antecedent of team effectiveness [41]. Thus, being aware of one’s
own and others’ emotional states could significantly contribute to project success [39, 75].
Inspired by these findings, we envision the emergence of tools and approaches to support
developers’ emotional awareness to improve their well-being and productivity. Previous work
advocated in favor of self-monitoring as a pathway to increase emotional awareness. Approaches
based on sensor logging [58] and self-reports [15] have been proposed to enable developers
and teams to self-monitor and reflect on their emotional experiences over time. Fritz et al. [21]
conducted a longitudinal field study with developers to examine the impact of a team nudge
intervention and found that frequent reflection on work and productivity can positively influence
individual productivity and reshape perceptions of teamwork and collaborative work. Ruvimova
et al. [74] conducted an exploratory study on how individuals perceive their team’s and their
own productivity. Their findings suggest that developers feel more productive when they perceive
their team as productive. However, the authors also noted a lack of awareness among developers
regarding the team’s productivity. While the approaches adopted in the literature may differ, the
main goal across these studies is to provide mechanisms for developers and teams to self-monitor
and reflect on their emotional experiences over time.
In this work, we focus on the study of self-monitoring of emotions in the context of agile
retrospective meetings, building upon previous research on the importance of emotion awareness
in agile development. Andriyani et al. [3] found that discussion of emotions is an important enabler
of reflection during meetings. Through interviews and observations of four agile teams’ retrospective
meetings, they identified discussing feelings, both positive and negative, as one of the key aspects
focused on. Along the same line, Madampe et al. [56] conducted a survey study with professional
agile developers to investigate the main challenges in handling requirements changes and how
these impact the emotions of software practitioners. They found that some challenges are technical
while others are social and could be addressed by leveraging emotional intelligence. Based on their
findings, they suggest that organizations, managers, and practitioners should consider regularly
implementing practices to support awareness of their emotional well-being. More recently, Milani
et al. [62] conducted a survey study with agile team members to investigate which data developers
share and how they used them in retrospective meetings. Most teams involved in their study
reported they prefer human-centric approaches over data-driven ones in retrospectives, stressing
the importance of discussing subjective data about feelings and work satisfaction. Overall, these


Self-monitoring of Developers’ Emotions 164:

studies demonstrate that embedding discussion of triggers for both positive and negative emotions
during retrospectives may be crucial to support agile development in many ways. In particular, this
practice may provide essential data for process improvement while helping teams identify systemic
issues affecting their performance [3]. Furthermore, sharing emotions is a practice that may create
opportunities for team learning and growth, and when properly facilitated with psychological
safety [3, 62], holds potential for strengthening team dynamics. Also, Milani et al. [62] suggest
enabling practices that proactively remind practitioners about key events and insights that might
be worth discussing during retrospective meetings.
In line with this vision, we complement previous work by investigating whether self-monitoring
of emotions during software development activities can enhance agile retrospective meetings.
Specifically, we examine whether this practice supports developers in recalling relevant emotional
episodes, reflecting on their causes, and identifying corrective actions for future development
sprints during retrospective sessions. To this aim, we designed and implemented EmoVizPhy,^1 a
tool to visualize data collected from non-invasive biometric sensors combined with self-reported
emotions and their causes [30]. We formulate ourresearch question (RQ)as follows:

RQ.Does self-monitoring of emotions enhance agile retrospective meetings?
To address this question, we conducted a controlled experiment using a crossover design with
experimental and control conditions. The study involved two teams of students and one team
of professional developers. In the experimental condition, participants used EmoVizPhy before
participating in the retrospective meetings to visualize the emotions experienced while working. In
the control condition, retrospective meetings were conducted without EmoVizPhy, adhering to the
teams’ usual practices. To evaluate the impact of emotions self-monitoring on retrospectives, we
measured both the number of cards contributed and corrective actions proposed by participants
in both conditions. Additionally, we conducted qualitative coding to categorize the corrective
actions defined by team members. To further assess the effects of our intervention, all study
participants were asked to take part in individual interviews and focus groups. We employed
thematic analysis to examine the qualitative data obtained from these sessions. Specifically, we
focused on the perceived usefulness of self-monitoring in supporting emotional awareness and
increasing the effectiveness of retrospective meetings. We also assessed the overall participants
experience, focusing on privacy concerns around using biometrics, self-reporting emotions, and
sharing emotion data with teammates.
Our empirical findings suggest that, under specific conditions, self-monitoring of emotions
through EmoVizPhy holds the potential to positively impact the effectiveness of retrospective meet-
ings. However, we observed mixed results for students and professional developers. In particular,
the proposed approach appears to foster more productive discussions concerning collaboration
and interpersonal dynamics among students—who lacked experience with agile practices and
worked in a newly constituted team—as well as the collective identification of related corrective
actions. Notably, the student participants in our study reported that using EmoVizPhy to visualize
self-reported emotions and biometric data helped them recall relevant emotional episodes, thus
leading to improved card writing and proposal of corrective actions for subsequent sprints. This was
not observed for professional developers—who were familiar with agile development and worked in
a consolidated team— who conversely reported mixed feedback regarding the perceived usefulness
of the tool for retrospective meetings. Therefore, we identify supporting the consolidation of new
teams in agile development as a promising use case for EmoVizPhy.

(^1) https://github.com/collab-uniba/emovizphy.


164:4 D. Grassi et al.

Furthermore, we observe that the participants in our study are mostly open to sharing their
emotions during retrospective meetings. In addition, the majority of students explicitly reported
the desire to keep monitoring emotions while working, thus confirming that novice developers
might perceive self-monitoring of emotions as more useful to increase emotion self-awareness
during software development tasks.
Finally, we identify challenges in the interpretation of biometric signals, highlighting the need
to combine them with contextual information, such as self-reported notes.
The main contributions of this article are as follows:
—We contribute empirical insights suggesting that self-monitoring of emotions may enhance
agile retrospective meetings, especially when novice developers are involved;
—We distribute an improved version of the EmoVizPhy tool, whose prototype usability was
evaluated in our previous work [30];
—We release a replication package including the EmoVizPhy tool, which is open source and
available for future research, as well as all the scripts and software instrumentation to enable
replication of this study.
The remainder of the article is structured as follows. In Section2, we report and discuss the
background knowledge on retrospective meetings in agile development, the theoretical model
of emotions we build upon in this study, and the use of biometrics for recognizing developers’
emotional and cognitive states. Then, we describe the design of our empirical study and explain
our methodological choices in Section3. We report the results in Section4 and discuss our findings
in Section5. The limitations and tradeoffs of the article are outlined in Section6. We position our
contributions in the scope of related work in Section7 and conclude the article in Section8.

2 Background

2.1 Agile Retrospectives

An agile retrospective is a structured meeting that takes place at regular intervals throughout a
project to help teams reflect on what went well, what did not, and how they can improve [13].
Unlike traditional project retrospectives, which occur only at the project’s end, agile retrospectives
happen iteratively, allowing continuous improvement [4]. Every retrospective is led by a facilitator,
who ensures that the team achieves the goals it sets [55].
According to Derby et al. [13], an agile retrospective involves five phases:setting the stage,
gathering data,generating insight,deciding what to do, andclosing the retrospective meeting.Setting
the stagefocuses on creating a safe and comfortable environment where team members feel
encouraged to share openly.Gathering datainvolves collecting information about the sprint,
including both quantitative data (e.g., metrics and completed tasks) and qualitative data (e.g.,
personal observations and feedback).Generating insightrequires the team to analyze the collected
data to uncover underlying issues and patterns.Deciding what to dofocuses on creating actionable
improvement plans.Closing the retrospective meetinginvolves summarizing the decisions and
acknowledging the participants’ efforts.
As a simplified process model, retrospective meetings follow a two-stage structure. In the
first stage, participants document all remembered events and experiences on cards, encouraging
comprehensive recall. The second stage involves grouping these cards and discussing them to
determine both corrective actions for the next sprint and successful practices worth continuing.
While the initial brainstorming may generate some less relevant items, the subsequent clustering
and focused discussion help filter and prioritize the most important insights. From a cognitive
perspective, the first stage of card writing can be assimilated to the generation of new ideas and


Self-monitoring of Developers’ Emotions 164:

then it primarily involves divergent thinking [12]. On the other hand, the second stage of action
proposal requires resolving individual views, sometimes opposing, and then it mainly involves
convergent thinking [59].
Different templates for conducting retrospective meetings exist [29], such as the Sailboat, Starfish,
One-Word Retrospective, and the Mad, Sad, Glad model. To conduct a retrospective using the Mad,
Sad, Glad model [13], the facilitator divides a board into three areas labeled “Mad,” “Sad,” and “Glad”
and provides color-coded cards or sticky notes. Participants write down their issues on sticky
notes and categorize them accordingly. Once the timebox expires, the sticky notes are posted in
the appropriate section. The team then groups related sticky notes into logical themes, which are
subsequently discussed. Based on these discussions, the team identifies specific actions to start,
stop, or continue in the upcoming sprint.
This model has been widely adopted in practice due to its effectiveness in releasing heavy
emotional steam and gathering data about feelings [13, 70]. For its focus on emotions, we adopt it
in our study.

2.2 Emotions in Software Development

Dimensional Modeling of Emotions. In the last decade, emotions experienced during software
development have gained increasing attention in software engineering research [9, 19, 38, 54,
64, 65, 68, 69]. Studies have been conducted on the effects of emotions on productivity [25, 26,
33, 63, 88], the relationship between emotions and problem-solving [34], and the relationship
between affective states and software metrics [50]. The majority of existing studies on the impact
of emotions on software development adopt a dimensional approach to emotion modeling [26, 27,
30, 63], which usually includes considering three dimensions for emotions, namelyvalence,arousal,
anddominance. Two of these dimensions are originally defined by Russel [73], whose Circumplex
Model of Emotions operationalizes affective states in terms ofvalence, i.e., the pleasantness vs.
unpleasantness of the emotional stimulus, andarousal, i.e., the emotional level of activation vs.
deactivation. Pleasant emotional states are associated withpositivevalence, while unpleasant ones
are associated withnegativevalence. In contrast, arousal refers to the level of activation of the
emotional state that ranges from inactive orlowtohigh. In line with previous studies [33, 57], we
adopt this dimensional modeling of emotions and also include consideration ofdominance, which
measures emotions according to the extent to which an individual feels in control of the situation.

Negative Emotions as a Proxy for Problems. Previous lab studies leveraged experience sampling
to identify the reasons for positive and negative emotions while programming [27, 35, 63]. They
found that developers experience negative emotions when their self-perceived productivity is low
while they feel happy when they are in flow. Other reasons for negative emotions are related to
cognitive difficulties, the impossibility of fulfilling information needs, and code not working. These
findings were complemented by further evidence collected in a field study involving professional
developers from five different companies, who contributed a taxonomy of triggers for both positive
and negative emotions at the workplace [26].
Graziotin et al. [31] further contributed to the identification of triggers for developers’ emo-
tions through a survey involving∼2K developers. They found that the most frequent causes of
unhappiness include being stuck in problem-solving, operating in condition of time pressure,
dealing with bad code quality or under-performing colleagues, feeling inadequate or suffering from
personal issues not related to work, dealing with bad decision-making or investing time in mundane
repetitive tasks. Girardi et al. [26] enhanced the body of knowledge on emotional triggers through
a field study involving professional software developers in their daily work setting. Their findings
further confirm that are relationship exists between positive emotions and perceived productivity.


164:6 D. Grassi et al.

Beyond emotional valence, specific emotions have been investigated. In particular, early de-
tection of non-positive emotional episodes might enable the identification and implementation
of just-in-time corrective actions aimed at restoring positive emotions and productivity. Thus,
it is not surprising that researchers mostly focused on negative emotions. Gachechiladze et al.
[22] investigated automatic approaches to anger detection in collaborative software development.
They focused on anger as it can serve as a proxy for a wide range of problems that might require
prompt resolution to support effective collaboration. Specifically, they distinguished between anger
toward self, which could be useful to identify and support developers experiencing difficulties,
anger toward others, which might be an indication of communication issues, and anger toward
objects, which could be a proxy for technical problems and could be helpful to recommend and
prioritize improvements. Ford and Parnin [18] surveyed 45 software developers to identify the
causes of frustration while programming. They provide a list of 11 categories, which include issues
with program comprehension or poor tooling, personal issues, and fear of failure.

Emotions in Agile Retrospective Meetings. Recent studies have demonstrated the crucial role
of emotion sharing in agile meetings and how this can support team effectiveness and process
improvement. Emotions in retrospectives serve a dual purpose: they provide valuable data about
team processes and contribute to team effectiveness. Andriyani et al. [3] conducted an interview
study with 16 developers adopting agile practices. They report that reflection in agile retrospectives
occurs across three levels: reporting and responding, relating and reasoning, and reconstructing,
with emotions being central to the reporting and responding phase. In particular, they provide
significant insight into why discussing negative episodes is essential for the reflection process.
Based on their empirical results, they suggest that reflecting on the challenges encountered during
the sprint is essential for the teams to understand process-related aspects, such as the effort required
to complete tasks, what tasks were challenging, and why some tasks were difficult to finish. This
indicates that negative situations serve as valuable learning opportunities and hints for reflection on
aspects that require interventions to support team effectiveness. In this perspective, by discussing
obstacles that trigger negative feelings, the teams can discuss crucial information needed for process
improvement. Similarly, positive feelings were reported in association of successful practices that
could be consolidated and readopted also in future sprints.
Girardi et al. [26] complemented these findings through a field study with companies implement-
ing agile development. Based on the qualitative analysis of developers’ responses to open-ended
questions about the causes of their self-reported emotions during programming, they built a taxon-
omy of specific triggers of positive emotions (such as being in flow or completing tasks) and negative
emotions (including difficulties with code comprehension or tooling issues). The authors suggest
that discussing these emotional triggers in retrospectives might help teams identify systemic issues
that could otherwise remain unaddressed over time.
In line with this view, Milani et al. [62] recently reported on the importance of integrating
both subjective emotional and objective project-related data to drive discussion in retrospective
meetings and identify improvements to implement. They ran an online survey study with 19
software development teams to explore how agile teams conduct retrospective meetings and utilize
data within these sessions. Their findings reveal that most teams engaged in pre-meeting activities,
including setting up tools, gathering metrics, and allowing members to add discussion topics in
advance. A significant finding was the strong reported preference for human-centric approaches
over data-driven ones. Only six teams reported using objective project data in retrospectives,
while nine explicitly mentioned relying on subjective data, including feelings, empathy, well-
being, and workplace satisfaction. Based on their empirical findings, the authors provide a set of
actionable insights, including a recommendation to support practitioners in data collection prior


Self-monitoring of Developers’ Emotions 164:

to the meeting. They emphasize the importance of gathering both subjective and objective data.
Furthermore, they suggest designing tools that enable proactive reminders to practitioners about
key insights to share during retrospective meetings. Along this line, El-Migid et al. [15] proposed
Emotimonitor, a Trello extension to enable emotion self-report by developers, demonstrating that
emotional feedback during retrospectives can trigger valuable insights for team improvement.

2.3 Stress in Software Development

Other psychological states associated with emotions were also investigated, due to their potential
impact on developers’ well-being and productivity. It is the case of time pressure, which has been
shown to have both positive and negative effects on software developers. On the positive side, it
can increase motivation. However, it also leads to negative consequences, such as increased stress,
unhappiness, depression, and burnout [49].
Among other psychological states that are associated with the experience of emotions, stress
deserves particular attention due to its observed correlation with negative emotions [16]. Lazarus
and Folkman [53] define stress as the relationship between an individual and the environment that
is assessed by the person as “taxing or exceeding his or her resources and endangering his or her
well-being.” Graßl et al. [36] investigated the impact of diversity on stress experienced by software
engineering students working in project teams. The study was conducted through three controlled
experiments involving 65 participants from two universities. The results show the main stressors
for the students were a missing work approach, time, and organization, which are also common
stressors in professional software development. Chow et al. [10] present a field evaluation of a
digital intervention designed to support knowledge workers in managing stress and improving
productivity. The authors conducted a 4-week exploratory study with 24 graduate students as
participants. The study introducedTherapy-inspiredintervention consisting of using the term “Time
Well Spent” instead of “Productivity,” a mobile self-logging tool for tracking activities, feelings,
and thoughts at work, and a visualization tool to facilitate reflection on the collected data. The
findings of the study indicate that participants who used the Therapy-inspired intervention had
an increased consideration of their well-being, including the importance of taking breaks and the
impact of their emotions.
Motivated by the empirical evidence provided in these studies, in this article, we also focus on
the identification of stress episodes, whose causes might inform the discussion, in retrospective
meetings, toward identifying corrective actions to be implemented in subsequent sprints.

2.4 Biometrics as a Proxy for Emotions and Stress

The link between emotions and biometrics has been investigated for a long time in affective
computing research. Specifically, changes in biometrics associated with the electrical activity of
the brain (EEG), the electrical activity of the skin (EDA), and heart-related metrics, such asblood
volume pressure (BVP),heart rate (HR), andHR variability (HRV)have been successfully
used for emotion detection [44, 46, 79].
In recent years, software engineering researchers investigated emotion detection using light-
weight biometric sensors that can be comfortably worn while coding [27, 63, 84]. Recognition of
negative emotions received special attention [26], as these might be detrimental to developers’
well-being and productivity [34]. Fritz et al. [20] relied on a combination of EEG, BVP, and eye
tracker to assess difficulty in code comprehension and prevent developers from introducing bugs. In
a follow-up study, they employed the same sensor set to distinguish between positive and negative
emotions while programming [63]. Along the same line, Girardi et al. used biometrics to classify
developers’ emotions during a lab study [27] as well as at the workplace [26]. Some studies have


164:8 D. Grassi et al.

dedicated attention to specific tasks. It is the case, for example, of Vrzakova et al. [84], who used
eye gaze and EDA for classifying developers’ valence and arousal during code reviews.
Sensor-based identification of stress episodes was recently investigated by Westerink et al. [86].
They demonstrated that a correlation exists between peaks of cortisol, which is the hormone
associated with the experience of psychological stress, and peaks of skin conductance (EDA). In
particular, EDA was observed to anticipate the peaks of cortisol, thus suggesting that peaks in the
EDA signal can be successfully used for the early identification of stress episodes. Kocielnik et al.
[45] visualized EDA data in combination with a user’s calendar and tried to reveal the association
between stress and activities.
Furthermore, other studies have investigated the use of heart-related metrics to assess stress
levels. For instance, the AffectiveWall [89] system utilizes HRV and the inter-bit interval to visualize
stress in real-time, facilitating self-awareness and stress management within groups during work.
Also, Yu et al. [90] used HRV to generate a tree-like image representing an individual’s stress levels
and overall health state. Participants found the visualization easy to understand, motivating, and
helpful for self-reflection on stress levels.
In our study, we consider EDA and HR, which can be collected using low-cost, non-invasive
sensors [24, 26, 63, 84] that can be comfortably used by developers during programming tasks. This
choice is in line with current research investigating the use of lightweight biometric sensors for
emotion recognition in software development [24, 63]. Specifically, we instructed the study partici-
pants to focus on peaks in the biometrics associated with stress when visualizing their emotions
with EmoVizPhy before retrospective meetings. We provide further details in the Methodology
(see Section3).

3 Study Design

In this section, we describe the design of our empirical study and the methodology we adopted to
quantitatively and qualitatively analyze the data we collected. In line with the primary goal of this
study, we have designed an experimental protocol to enable a direct comparison of retrospective
meeting outcomes in a control condition with meetings performed under the experimental condition
involving emotion monitoring. We start by describing the groups of participants involved in the
research: undergraduate software engineering students and professional software developers (see
Section3.1). To clearly explain the methodology adopted in this study, we first present the self-
monitoring tools adopted in the experimental condition in Section3.2. Then, in Section3.3 we
describe the full experimental protocol, including the study duration, its crossover design, the study
setup, and the data collection approach. In Section3.4, we explain the quantitative and qualitative
approach adopted for analyzing the data. Finally, we conclude this section by illustrating how the
study design was refined through a pilot and report the details of the experimental protocol.

3.1 Participants

Software Engineering Students. For the first part of the study, we recruited 10 Italian undergrad-
uate computer science students aged between 20 and 25 years; among them, seven identified as
male and three as female. At the time of the study, they all possessed limited to no professional
experience in agile development. Furthermore, the teams involved in the study were just created
for the capstone project, and their members had no previous experience in collaboration as a team.
As such, they can be seen as representative of novice developers working in a new team, with roles
and team dynamics still being defined.
The execution of this project was organized into three Scrum sprints—each lasting 2–3 weeks—with
the students assigned to teams of five members each. On average, students declared to invest be-
tween 5 and 10 hours per week in the course, equivalent to 10–20 hours per sprint. No one was


Self-monitoring of Developers’ Emotions 164:

```
Fig. 1. The Empatica E4 wristband.^2
```
familiar with the agile approach nor with Mad/Sad/Glad. The project task revolved around collabo-
ratively building a command-line game in Java. All team members were invited to contribute to their
prototype’s development by adopting well-established software engineering best practices, tools,
and workflows. For instance, the students used GitHub as a collaborative development platform,
leveraging its issue-tracking system and the GitHub flow as a development workflow.
At the beginning of the Software Engineering course, the experimenters explained the study
protocol to all course attendees and sought volunteers interested in joining the research; a web form
was used to collect contact details of the student volunteers. Among 80 volunteers, we selected only
those belonging to teams in which all team members were available to join the experiment—indeed,
we aimed to include full teams in the study. Specifically, three teams out of 39 were enrolled in the
experiment, one of which only participated in the pilot study (see Section3.5) and two in the actual
study (see Section3.3). At study completion, all students were rewarded with a meal voucher.

Professional Software Developers. For the second part of the study, we recruited a team of four
professional software developers who work for a software consulting company in Italy. All team
members were Italian and aged between 25 and 35 years; three of them identified as male and
one as female. The team comprised two senior developers with a BSc in Computer Science and
6–8 years of experience, one junior developer with a high-school diploma and less than 2 years of
experience, and a mid-level developer with a high-school diploma and 2–4 years of experience.
After participating in the initial days of the experiment, the junior developer (aged between 18 and
25 years, identified as male) had to take leave for personal reasons. As a result, we were unable
to collect survey responses or to conduct an interview with them. Therefore, we will report only
the data from the three professional developers who completed the entire experiment. It is worth
noting that all teams in the company adopt an agile software development methodology.

3.2 Self-monitoring Tools

Here, we describe the self-monitoring tools employed in our study, involving three components:
biometric data collection, self-reporting of emotions, and visualization of both data sources.

Empatica E4. To collect biometric data, we used Empatica E4^2 (see Figure1), a wristband
equipped with EDA and BVP sensors, where the latter is used to derive HR and HRV. EDA and
BVP signals are recorded with a sampling frequency of 4 Hz and 64 Hz, respectively. In this study,
we plot the EDA signal, as its peaks are reliable proxies for stress episodes [86], and the HR to
complement the visualization for better stress identification [89, 90].
Physiological signals obtained with wearable sensors may contain noise due to events unrelated to
the phenomenon being investigated, such as electrode contact loss or movement of the participants.
As a result, the raw signals recorded during the experimental sessions need to be cleaned to allow

(^2) Image fromhttps://www.empatica.com/en-eu/research/e4/.


164:10 D. Grassi et al.

for meaningful data interpretation with respect to the cognitive and emotional mental states of the
participant. To this aim, we use the tool by Taylor et al. [81] to identify and remove artifacts in
the EDA signal, i.e., peaks due to noise rather than genuine changes in skin conductance values.
We compute EDA peaks using the same tool, which implements a method capitalizing on the first
derivative of the signal curve. The choice to incorporate the identification of signal peaks is based
on the findings by Westerink et al. [86], who demonstrated that stressful events are associated with
EDA peaks.
For what concerns the HR signal, we do not apply any filtering technique as the data are not
obtained from a real-time reading, but derived from the BVP signal through Empatica’s algorithms.^3

Self-report of Emotions. To enable the self-reporting of emotions, we replicate the experience
sampling approach [52] adopted in previous studies to collect participants’ emotions and activi-
ties during the execution of programming tasks [26, 27, 63]. Specifically, we leverage the popup
application developed by Girardi et al. [27], which the authors made publicly available.^4
The configuration of the popup application for the self-report aligns with the experimental
protocol adopted by Girardi et al. in their field study on developers’ self-reported emotions and
perceived productivity in the workplace [26]. In particular, the popup questionnaire relies on the
Self-Assessment Manikin (SAM) technique to prompt the subjects for emotion self-reporting [5],
employing a 5-point pictorial scale to request a score for each emotional dimension, i.e., valence,
arousal, and dominance (see Figure2). Besides, the popup prompts the subjects to report their
current activity by selecting an item from a drop-down list. Based on previous work [26, 60], we
included the following items in the list:coding, bug fixing, testing, design, meeting, e-mail, helping,
networking, learning, administrative task, documentation, just arrived, and other. Additionally, the
popup includes a free-text notes field where participants can optionally write down notes to explain
the self-reported emotions and to elaborate further on their causes. A notification, asking to fill out
the self-report form, is presented periodically to the subjects. The timing of these notifications can
be adjusted: By default, the popup appears on the participant’s monitor once every 30 minutes, and
we used this interval in the experiment with the students. However, developers explicitly requested
to limit interruptions as much as possible, so we set the interval to 60 minutes in their case. Each
time, the subject can decide whether to answer immediately or postpone the notification in a range
between 5 and 120 minutes. An option to fully discard the popup notification is also provided, in
which case it is up to the subject to decide when to resume the popup dialog.
In total, participants contributed 249 pop-up entries during the study (117 for students and
132 for practitioners), of which 80 also contained notes (50 for students and 30 for practitioners)
explaining the cause for the self-reported emotion. On average, during the whole study, students
answered 12 popups and eight notes each, while practitioners contributed 33 popups and eight
notes each. The participants individually accessed the self-report information through EmoVizPhy,
before retrospective meetings, to recall relevant episodes. Among the students, the number of days
without any recorded popup responses ranged from 0 to 6. For practitioners, only two participants
had a single day each without submitting any responses.

Emotion Visualization. To enable the visualization of the collected data during agile retrospective
meetings, we extended EmoVizPhy, an open source prototype developed in our previous work [30].
EmoVizPhy is designed to support emotion awareness in the workplace through the visualization of
self-reported emotions and biometrics recorded during software development activities. Concerning
biometric signals, the original interface by Grassi et al. [30] could only plot data related to EDA. To

(^3) https://www.empatica.com/blog/decoding-wearable-sensor-signals-what-to-expectfrom-your-e4-data.
(^4) https://github.com/collab-uniba/ExperienceSampling.


Self-monitoring of Developers’ Emotions 164:

Fig. 2. Self-report popup interface. It includes a drop-down list for activity selection based on predefined
categories, valence, arousal, dominance ratings, self-perceived productivity scale, and a free-text notes field.

provide a richer visualization, we extended the tool by incorporating the HR signal (see Figure3).
While adding more signals could potentially increase the cognitive load on users, prior research has
shown that the visualization of heart-related metrics can provide valuable insights into affective
states such as stress [89, 91].
Note that the plot of both signals might not necessarily align. Although both EDA and HR signals
are modulated by the autonomic nervous system, they respond to different stimuli and operate
on distinct timescales [23]. Figure3 shows an example of the interface of EmoVizPhy. The top
panel displays the EDA signal over time. Vertical lines mark EDA peaks, corresponding to moments
that may signify stress, in line with evidence provided by previous work [86]. The bottom panel
presents the HR signal, measured in beats per minute. Changes in HR can be mediated by both
the sympathetic and parasympathetic nervous system [28] and may indicate emotional responses
[7]. In particular increase in HR is observed during the stress exposure [48, 71]. In both plots,
hovering over a specific point in the timeline reveals a detailed tooltip with contextual information,
such as the participant’s activity, self-reported valence and arousal levels, dominance, perceived
productivity, and notes.
Moreover, to aid the navigation of biometrics and self-reports collected over 2-week periods, we
made the plots interactive, enabling actions like resizing and panning. Also, we added buttons for
saving images, zooming, and toggling the display of additional data-point information on mouse
hover.

3.3 Experimental Protocol

Study Duration. All teams participated in the study for two agile iterations, which were 2 weeks
long. As for the student teams (Teams A and B, hereinafter) operating in the scope of the Software
Engineering Course, we employed a crossover design (see Figure4). In Sprint 1, Team A was
assigned as the experimental group, meaning that its members wear the Empatica E4 wristband and


164:12 D. Grassi et al.

Fig. 3. EmoVizPhy Interface: the top panel shows the EDA signal over time, with vertical lines highlighting
peaks. The bottom panel presents the HR signal. Tooltips provide contextual information, including self-
reported valence, arousal, dominance, perceived productivity, and notes. In the example shown, the participant
contributed a note explaining that a merge conflict was just resolved and reported high emotional valence
and arousal. Indeed, earlier peaks in the EDA signal may indicate moments of stress while the participant
was actively working through the merge conflict. Conversely, the EDA plot associated with the self-report
appears flat, and no evidence of peaks is observed, which suggests the self-report was made in a less stressful
condition.

utilize the pop-up application, while Team B functions as the control group, in which information
about emotions and biofeedback is not collected. In Sprint 2, the roles are reversed, with Team A
serving as the control group and Team B as the experimental group. The teams are required to
follow the Scrum methodology, including the organization of a retrospective meeting at the end
of each iteration. Before starting the study, the experimenter conducted two separate meetings
with the two student teams participating in the study. These meetings did not involve the use of
EmoVizPhy. The purpose of these meetings was to help participants familiarize themselves with
the retrospective meetings and, in particular, with the Mad/Sad/Glad model.
As for theprofessional developers, the team was already having retrospective meetings at the
end of each development iteration, which was one-week long. Overall, the team participated in
the study for two weeks, both in the experimental setting. Differently from what was done for the
student teams, the control condition here is the usual protocol adopted by the team for running
their retrospective meeting, which does not involve the use of EmoVizPhy.

Study Setup. The same experimental setup was employed with both students and professional
developers. The day before the experiment, the experimenter met with the participants. During
this preliminary meeting, the participants signed the informed consent forms,^5 acknowledging the
purpose, procedures, and data handling processes of the study. Then, the experimenter demonstrated
how to properly wear the wristband, install the popup application, use the E4 Manager software to

(^5) Ethical review board: ERB2023MCS31, Eindhoven University of Technology, The Netherlands.


Self-monitoring of Developers’ Emotions 164:

```
Fig. 4. Experimental protocol for the data collection during the sprints.
```
download raw biometric data from Empatica E4, and share this data with the research team via a
private OneDrive channel.

Data Collection. Participants wear the Empatica E4 wristband and use the popup application
while performing their work activities. In particular, the students were asked to do so while
working on their capstone project and pause the monitoring while performing other activities (e.g.,
attending classes). Professional developers, on the other hand, were asked to wear Empatica E4 and
periodically answer the questionnaire in the popup during the entire working day, as they were
involved in a single project full-time. In both settings, participants can postpone answering the
popup if they do not want to be interrupted. To further reduce the intrusiveness of the popup, we
allow participants to dismiss it for the entire day. On the other hand, participants are enabled to
invoke the popup manually, for instance when they experience strong emotions that they believe
are important to report. At the end of each working session, they turn off the device and share data
with the experimenter who reviews them to check for consistency and completeness.

Retrospective Meeting. At the end of each sprint, a retrospective meeting is held in both the
experimental and control conditions. Before the experimental retrospective meetings, the exper-
imenter individually presents the EmoVizPhy visualizations to each participant, allowing them
to explore the data sessions and, if desired, take notes on events and patterns to share with the
other team members. Figure5 shows a five-stage process for conducting our empirical study for
both students’ and professionals’ teams operating in the experimental condition. The process
starts with participants reviewing individually (for up to 15 minutes) the emotional data using
EmoVizPhy. This individual activity is performed before entering the meeting to gain insights and
recall episodes that could potentially inform card writing during the meeting. After this individual
phase, a regular retrospective meeting starts with the entire team (see Figure6), following the
traditional steps described in Section2. In the control condition, the retrospective meeting was
conducted without the use of EmoVizPhy. In both conditions, we documented the cards contributed
by meeting participants, which reflected their perspectives on the sprint, as well as the corrective
actions collaboratively identified and defined by the team to enhance quality and efficiency in
subsequent sprints.


164:14 D. Grassi et al.

Fig. 5. Five-stage empirical study process transitioning from individual activities to collaborative retrospective
meeting.

Fig. 6. Student participants during a retrospective meeting. Different colors of cards are used to distinguish
between mad, sad, and glad, i.e., pink, yellow, and blue, respectively.

Interview and Focus Group. To thoroughly understand the perceived usefulness of EmoVizPhy,
we conducted individual, semi-structured interviews with all the study participants and three
focus groups at the end of the experiment. Focus groups allowed us to observe how participants


Self-monitoring of Developers’ Emotions 164:

discussed and reflected on their experiences collectively [1], which was especially relevant given
that retrospectives are typically group activities. At the same time, individual interviews helped
us explore more personal views in greater detail, including aspects that might not emerge in a
group setting [87]. Using both methods enabled us to capture a broader range of perspectives—both
shared and individual. Similar mixed-method designs have been used in related work, such as
by Wang et al. [85], who applied interviews and focus groups in the evaluation of Adaptive User
Interfaces in mobile health contexts.
Six of our interview questions required participants to provide answers on a 4-point ordinal scale
and to elaborate on their responses. All interview questions are reported in AppendixA, which
presents the interview guide. The experimenter conducted all interviews immediately following
each experimental retrospective meeting, with each session lasting between 15 and 30 minutes.
Additionally, at the end of the study, we carried out three focus groups: two with the two teams
of students and one with the team of professional developers (see AppendixB for the focus group
guide). The focus groups were conducted by the experimenter and lasted between 30 and 45 minutes.
Both during the interviews and the focus groups, the experimenter took notes and made an audio
recording of each session. Afterward, we transcribed the audio recordings and coded the transcripts.

3.4 Analysis

Analysis of Cards and Corrective Actions. As part of our analysis, we examined the cards and
corrective actions collected during the retrospective meetings. First, we compared the number
of cards written and corrective actions proposed by team members across both the control and
experimental conditions. Subsequently, we conducted a qualitative analysis of the corrective actions
identified by each team. In particular, we applied a closed qualitative coding approach, categorizing
each corrective action as relating to either “process,” “people & relationships,” or “tools,” following the
definitions provided by Dingsøyr et al. [14]. It is noteworthy that the coding scheme of Dingsøyr
et al. includes two additional codes—i.e., “projects” and “other teams”—designed specifically for
large-scale agile development contexts. These categories were not applicable in our study, as our
focus was exclusively on small agile teams.
Three authors independently assigned codes to each of the 39 corrective action documented
from the retrospective meetings. To assess inter-annotator agreement, we calculated Fleiss’ kappa,
obtaining a value of 0.85, which indicates almost perfect agreement according to the classification of
Landis and Koch [51]. The three coders then convened to discuss and resolve the few disagreements,
reconciling five discrepancies among the 39 actions.

Qualitative Analysis of the Participants’ Feedback. Another essential component of our analysis
is the qualitative examination of the interview and focus group transcripts, which we conducted
using thematic analysis [6]. As a first step, the first author gained familiarity with the collected
material by carefully reading the transcripts and actively seeking meanings and patterns in the text.
Next, she extracted 167 excerpts from the transcripts based on their relevance to our RQ. Sentences
reporting irrelevant contextual information (e.g., details about the Software Engineering course)
as well as passages concerning personal subject information or anecdotes were ignored—e.g.,: “In
general, I liked this experience because I understood things that I otherwise would not have known...
for example, what is a PhD; and I could see what it means to do research and work in this field” (S3).
Afterward, the first author carried out a round of open coding, freely assigning a code to each
excerpt. All codes were noted down into a codebook, along with their definitions. This initial open
coding process resulted in 20 codes.
Later, the codebook was discussed and refined by the whole research team during a plenary
meeting. Subsequently, the first and the third authors engaged in a round of focused coding, in


164:16 D. Grassi et al.

which they independently tried to assign the codes from the refined codebook to the 167 transcript
excerpts. Whenever they could not identify a suitable code from the codebook to classify an excerpt,
they would use the extra code “OTHER”; similarly, if they felt an excerpt had been included by
mistake, e.g., because it was not actually relevant to the study research goal, they would use the
extra code “DISCARD.” To assess the inter-coder agreement in this first round of focused coding,
we calculated Cohen’s휅and obtained a value of 0.76 (representing a “substantial” agreement,
according to the classification of Landis and Koch [51]). Despite this, 30% of the excerpts (57 in
total) were assigned different codes by the two coders. These discrepancies were subsequently
resolved in a new meeting involving the whole research team. Also, the team discussed whether
to actually discard the excerpts marked with the “DISCARD” extra code by at least one coder as
well as which code to assign to the excerpts marked with “OTHER.” As a result, the codebook was
further refined and a couple more codes were introduced, resulting in a total of 22 codes.
To account for these changes in the codebook, the two coders engaged in a second round of
focused coding, leveraging the updated list of codes and definitions. This time we computed a
Cohen’s휅of 0.94 (representing an “almost perfect” agreement according to the classification of
Landis and Koch) and a disagreement of 5% (9 excerpts). Moreover, none of the coders felt the need
to resort to the “OTHER” or “DISCARD” extra codes this time, thus increasing our confidence in
the completeness of the last codebook revision, which includes 25 codes.
The two authors involved in the coding activity discussed about how to best organize the
identified codes into themes and wrote a tentative list of themes and related definitions. Then, the
final version of the codebook and the resulting themes were thoroughly reviewed by the whole
research group to ensure consistency and soundness. Ultimately, the qualitative analysis resulted
in the definition of the taxonomy described in Section4.

3.5 Pilot Study

To consolidate our study design, we conducted a pilot study involving a team of five students from
the Software Engineering course, separate from those involved as the actual study. The pilot was
executed while these students were dealing with the first of the three agile iterations planned for
their capstone project. The students were asked to wear the Empatica E4 wristband and to utilize
the popup self-report application while carrying out their project activities.
The purpose of the pilot was to evaluate and identify any potential issues with the experimental
procedures or equipment. At the end of the sprint, a retrospective meeting was conducted following
the Mad/Sad/Glad template [13].
During the meeting, the experimenter played the role of the scrum master, facilitating the
discussion. She started by introducing the EmoVizPhy tool and encouraging the participants to
explore it. Afterward, she solicited the participants to write personal cards reflecting on their
experiences during the sprint. Subsequently, the experimenter read aloud the cards and proposed
thematic clusters for cards addressing similar issues. Following the conclusion of the retrospective
meeting, the experimenter conducted individual follow-up interviews with the students. The pilot
participants confirmed that reporting emotions through the popup tool was not annoying and
that the Empatica wristband was comfortable to wear. In addition, they recommended sharing the
EmoVizPhy installation files and instructions on the day before the actual retrospective meeting,
allowing time for the installation of the tool.

4 Results

Here, we present the results of our quantitative and qualitative analyses. In Section4.1, we re-
port on the quantitative assessment of the retrospective meetings in our study, focusing on the
number of cards contributed and corrective actions proposed. To provide deeper insight into the


Self-monitoring of Developers’ Emotions 164:

```
Table 1. Comparison of the Number of Cards Written and the Corrective
Actions Proposed during Retrospective Meetings in Both Control and
Experimental Sprints by the Teams of Students and Professional Developers
```
```
Team
Control Sprint Experimental Sprint(s)
Cards Actions Cards Actions
Student Team A 21 5 21 9
Student Team B 17 6 20 7
```
```
Professional developers 9 3
```
### 18 3

### 13 5

```
The professional developers conducted two experimental sprints.
```
influence of self-monitoring, we then conduct a qualitative coding of the proposed corrective
actions, as these represent the most significant and tangible outcomes of retrospectives. In Section
4.2, we report the results of our qualitative analysis of the interview and focus group transcripts.
This analysis provides a nuanced perspective on whether, and how, emotion self-monitoring via
EmoVizPhy could enhance agile retrospective meetings. To address potential concerns related to
tool usability, in our interviews and focus groups, we also gathered feedback regarding theuser
experience (UX), specifically regarding the Empatica E4 wristband, the self-report application,
and EmoVizPhy. Participants’ UX feedback is outlined in Section4.3. Finally, in Section4.4, we com-
ment on the survey responses provided by the study participants to the ordinal-scale items in our
interview guide.

4.1 Analysis of Meeting Outcomes

During retrospective meetings, team members reflect on the completed sprint by recording their
observations on cards and engaging in collective discussion. Subsequently, the team collabo-
rates to identify and define specific corrective actions to implement in future sprints. Given that
the primary objective of a retrospective is to plan strategies for improving quality and effec-
tiveness [76], the most immediate and tangible outcome of the meeting is the set of agreed-
upon corrective actions. In particular, team members produce a set ofContinueitems—practices
or behaviors that proved effective during the sprint and should be maintained in future itera-
tions. Alongside these, they identifyStopactions, which are ineffective practices that should be
eliminated, andStartactions, which are new strategies or improvements to be introduced in
upcoming sprints.
The number and quality of these actions can serve as strong indicators of meeting success.
Consequently, these indicators provide a basis to objectively evaluate our RQ concerning whether
the self-monitoring of emotions enhances agile retrospective meetings. Below, we compare the
number of cards written and corrective actions proposed by team members under both control and
experimental conditions (see Table1). Next, we present the findings of our qualitative analysis of
the corrective actions defined by each team. The results are reported separately for student teams
and professional developer teams (see Table2).

Students.Students in Team A wrote an equal number of cards in both the control and experi-
mental sprints, but nearly doubled their proposed corrective actions, increasing from five to nine.
Students in Team B contributed three additional cards in the experimental sprint (rising from 17 to
20) and proposed one more corrective action (increasing from six to seven).


164:18 D. Grassi et al.

```
Table 2. Distribution of Proposed Corrective Actions by Code for
Students and Professional Developers, as Identified through Qualitative
Closed Coding
```
```
Students
People/Relationships Process Tools
Control sprint 5 7 0
Experimental sprint 9 4 3
```
```
Professional Developers
People/Relationships Process Tools
Control sprint 1 2 0
Experimental sprint 1 0 2 1
Experimental sprint 2 0 5 0
```
Examining the distribution of corrective actions for both student teams, besides a total increase of
five actions (from 11 to 16), we observed notable shifts across coding categories. In particular, actions
categorized under “people & relationships” increased by four, from five to nine. During the control
sprints, proposed actions were primarily focused on cultivating a positive and empathetic work
environment (e.g.,Continue: “Keep a positive environment,”Stop: “Do not make team members feel
obligated to complete a specific task by a set deadline.”) as well as enhancing the team’s commitment
to high-quality work (e.g.,Stop: “Doing superficial work”). In the experimental sprints, additional
actions were defined to further promote a cohesive and empathetic team dynamic (e.g.,Continue:
“Work as a team,”Start: “Take the time to listen when others share their problems,” andContinue:
“Altruism within the group”).
Conversely, actions related to “process” decreased from seven to four. In the control sprints, these
actions primarily addressed project management improvements (e.g.,Start: “Effectively manage
task dependencies to ensure that no team member is ever blocked.”) and maintaining team alignment
(e.g.,Stop: “Routinely postponing meetings”). In the experimental sprints, proposed actions still
concerned project management (e.g.,Stop: “Avoid overloading team members with tasks”) but also
the quality and timeliness of code reviews (e.g.,Stop: “Stop making checks at the last minute.”).
Furthermore, although no actions were assigned the “tool” code in the control settings, three
tool-related actions emerged during the experimental settings, primarily highlighting the need to
learn new tool or programming language features.

Professional Developers.The number of cards written by professional developers increased
noticeably, from nine in the control sprint to an average of 15.5 across the two experimental sprints.
Conversely, the number of corrective actions showed a modest increase, from three in the control
sprint to an average of four in the experimental sprints.
A closer examination of corrective action categories reveals further insights. Notably, no correc-
tive actions in the experimental sprints were categorized under “people & relationships,” a slight
decrease from the single action observed in this category during the control sprint (Start: “Ask for
support (delegate) if we’re short on time.”). The number of “process”-related corrective actions, which
stood at two in the control sprint, remained unchanged in the first experimental sprint and then
increased to five in the second experimental sprint. Specifically, in the control sprint, these actions
focused on encouraging team members to communicate their availability upon task completion


Self-monitoring of Developers’ Emotions 164:

```
Table 3. Taxonomy of the Themes and Codes from the Qualitative Analysis of Interview
and Focus Group Transcripts
```
```
Themes Codes S P
Developer’s attitude
```
```
Willingness Positive feedback S1, S2, S3, S4, S7, S9 P1, P2, P
to share emotions Negative feedback S5, S6, S8, S10 -
Privacy No concerns S1, S2, S3, S4, S5, S7, S8, S9, S10 P
Concerns - -
```
```
Emotion
representation
```
```
Interpretability of biometrics Positive feedbackNegative feedback S1, S3, S6, S7, S10S2, S3, S4, S5, S8 P3-
Peak-event association FeasibleChallenging S2, S3, S5, S6, S7, S8, S9, S10S6 P1, P3P1, P
Importance of notes S2, S3 P
```
```
Perceived usefulness
for retrospective
meetings
```
```
Focus and productivity boost S1, S10 -
Improved card writing Positive feedbackNegative feedback S4, S5, S6S2, S4 P1, P2P
Improved actions proposal Positive feedbackNegative feedback S4, S5S2 P
Improved emotional awareness Positive feedbackNegative feedback S1, S3, S4, S5, S7, S9, S10S4, S6, S7 P3-
Promising use cases - P1, P2, P
Desire to keep monitoring emotions S1, S3, S4, S5, S6, S7, S8, S9, S10 -
```
For each code, the table lists the participants who shared related excerpts, divided into two groups: students (S) and professional deve-
lopers (P).

and on preventing the initiation of new projects while requirements analysis remained at a high
level of abstraction. In contrast, in the experimental sprints, corrective actions primarily targeted
improvements in preparing for customer demos (e.g.,Start: “Prepare demos well in advance,”Stop:
“Performing code merges immediately before critical moments,”Start: “Attempting a production build
after any architectural change in the project”). Additional resolutions included limiting the number
of files in pull requests and continuing to prompt clients on blocking issues.
Finally, a single corrective action in the second experimental sprint was categorized as “tool”-
related, addressing the maximum resolution permitted for mockups in the project.

```
In Summary. For students, self-monitoring emotions during retrospectives was associated
with an increased focus on team relationships and empathy, with “people & relationships”
corrective actions rising from five to nine while process-focused actions decreased. For
professional developers, we observed that self-monitoring emotions was associated with
more detailed reflection (nearly doubling their written cards) but with less emphasis on
interpersonal relationships, as they shifted their corrective actions away from “people &
relationships” toward process improvements, particularly around customer demos and code
management.
```
4.2 Qualitative Analysis of the Interview and Focus Group Transcripts

In Table3, we present the taxonomy of themes and codes identified through qualitative analysis,
along with the lists of participants—students (S) and professional developers (P)—who provided
excerpts associated with each code. Where relevant, we established sub-codes to differentiate
between positive and negative feedback regarding the concepts underlying each code. Three themes
emerged from clustering the codes:Developer’s attitude,Emotion representation, andPerceived
usefulness for retrospective meetings.


164:20 D. Grassi et al.

Developer’s Attitude. This theme captures the participants’ attitudes toward using EmoVizPhy
and the overall process of emotion self-monitoring. It includes the codesWillingness to share
emotionsandPrivacy. Most participants manifested a positive outlook.
In particular, nine subjects (six students and all three professional developers) expressed their
Willingness to share emotionswith colleagues during retrospective meetings; one of the students
explicitly stressed the importance of honesty in a team: “During the retrospective meeting, I wanted
to be honest. I believe that honesty is a fundamental quality in a team. I hope that others have also been
sincere” (S7). This finding is in line with previous work [15] showing that developers are willing to
share emotions with their colleagues and that this information can be used to inform the discussion
during retrospective meetings.
Conversely, four students reported withholding their emotions during retrospective meetings.
Two of them refrained from expressing negative emotions as they felt these emotions were no
longer important after resolving the underlying practical issues. Similarly, one student chose not
to share brief episodes of anger, recognizing them as fleeting and insignificant. Another student
decided against revealing negative emotions to avoid criticizing his colleagues and to protect the
team’s cohesion.
As forPrivacyissues potentially associated with the use of biometrics and the collection of
emotion-related data, these did not emerge as critical among the study participants. Those who
explicitly mentionedPrivacy(nine students and one professional developer) felt quite at ease with
the subject and did not report any related concerns (see Table3).

```
In Summary. Most participants showed willingness to share emotions with colleagues during
retrospective meetings, emphasizing the value of honesty in team dynamics. However,
four students reported selective emotional disclosure, particularly withholding negative
emotions when they felt the underlying issues were resolved or to maintain team harmony.
No participants expressed significant privacy concerns about the collection of biometric
and emotional data in this study.
```
Emotion Representation. This theme addresses the participants’ perceptions of how their emo-
tions were represented through the visualization of biometric signals and the self-reported data. It
includes the codes:Interpretability of biometrics,Peak-event association, andImportance of notes.
The codeInterpretability of biometricscaptures participants’ views on the ease of interpreta-
tion of the biometric signals as visualized in EmoVizPhy. Five students found the visualizations
user-friendly and easy to interpret. In contrast, six participants—including five students and one
professional developer—reported challenges in understanding the visualizations. These difficulties
were mainly due to the lack of familiarity with the biometric signals. The professional developer
stated: “The visualization tool is nice, but you have to know how to read the biometric signal to fully
understand and interpret it” (P3). In light of this, other participants recommended including a
legend or providing guidelines to help with signal interpretation. This is in line with previous work
showing that the interpretation of biometric signals can be challenging for individuals lacking
expertise or experience in biometrics [40].
The codePeak-event associationrefers to the subjects’ ability to recall the cause of an emotion by
associating the peaks in the EDA signal to specific experiences or activities. We remind the reader
that—in line with the outcome of previous empirical research [86]—we use the EDA signal peaks as a
proxy for stressful events. Ten participants (eight students and two professional developers) deemed
the taskfeasibleand reported successfully linking the EDA signal peaks with their likely triggering
events. For instance, one student stated: “There was one particular session I remembered because we


Self-monitoring of Developers’ Emotions 164:21

had a lot of problems. We couldn’t resolve some issues highlighted by SpotBugs and Checkstyle, so
I texted a colleague to ask for his help. Seeing all those peaks reminded me of that specific episode.
Indeed, I even went back to check the dates of my messages, and they were sent exactly at the time we
were facing those errors and the EDA peaks were recorded” (S5). Conversely, three participants (one
student and two professional developers) considered the peak-event association taskchallenging.
They all noted a discrepancy between the peaks in the biometric signals and their actual emotional
experiences; interestingly, one student and one professional developer provided mixed feedback
on this topic. The latter found the process challenging, as they were unable to explain some of
the spikes in the EDA signal: “it seemed like some things matched and others didn’t. For instance,
there were moments when it seemed I was more agitated, but in reality, I know I wasn’t” (P1). Despite
these challenges, they still managed to identify some associations: “I remember before a meeting... I
was quite nervous... and at that time there was a spike [in the plot]” (P1). Similarly, the student also
faced difficulties with the peak-event association task: “I saw the stress peaks, but since I couldn’t
remember what I was doing at that time, I wasn’t able to link them to specific activities or reasons”
(S6). Nonetheless, they could still identify associations between certain peaks and specific events:
“For instance, when we all gathered together in the afternoon on the 16th, we all noticed spikes with
similar timings [in our plots]. We noticed the peaks of anxiety and tension...” (S6).
The codeImportance of notesconveys the opinion of three participants (two students and one
professional developer) who emphasized the need to complement biometric signal visualizations
with self-reported notes. When present, these notes helped them recall the causes of their emotional
states. For example, P3 reported: “Overall, the notes are an important way of complementing the
plots. Plots alone might not give you enough information unless you are able to access also the activity
performed at a specific moment in time. Being able to read own self-reported notes is useful in this
sense, as it helps you recall episodes that are worth mentioning in the retrospective meeting.”

```
In Summary. Participants had mixed experiences with biometric signal interpretation, high-
lighting the need for better visualization guidelines. Most of them successfully associated
EDA peaks with triggering events, though some noted discrepancies between signals and
emotional experiences. Self-reported notes proved useful for complementing biometric
data, enabling better recall of emotional episodes during retrospective meetings.
```
Perceived Usefulness for Retrospective Meetings. This theme encapsulates participants’ views on
the usefulness of the proposed self-monitoring tools in improving the effectiveness of retrospective
meetings. It encompasses codes that detail specific benefits of the proposed tools as reported by
the study participants (i.e.,Focus and productivity boost,Improved card writing,Improved actions
proposal, andImproved emotional awareness) as well as a code outlining furtherPromising use cases
of EmoVizPhy and one expressing participants’Desire to keep monitoring emotionsin the future.
The crossover design of our study, in which all participants experienced both the control and
experimental conditions, played a crucial role in enabling them to make informed comparisons
between traditional retrospective meetings and those augmented with the proposed self-monitoring
tools. Indeed, most of the excerpts supporting the codes within this theme stem from participants’
comparative observations enabled by this design.
Two students reported improvedFocus and productivity boostas side effects of participating in
the study and using the self-monitoring tools. In particular, they highlighted the positive impact of
wearing Empatica E4 on their perceived productivity. For instance, S1 stated: “I felt more productive
while wearing the sensor, it motivated me to work harder” (S1). The same student also reported that:
“Answering to the popup questions let me reflect on how I was feeling in that moment. It helped me


164:22 D. Grassi et al.

organize my thoughts” (S1). This evidence aligns with findings of recent work by Mayer et al. [61],
which demonstrate that self-reflection can enhance developers’ awareness of goal achievement
and productive habits by enabling them to evaluate progress and refine goals as needed.
The codeImproved card writingcaptures participants’ views on the ability of EmoVizPhy to
enhance the card writing activity during retrospective meetings. Four participants—including three
students and one professional developer—provided positive feedback in this regard. Specifically,
they emphasized that the visualization of emotional data facilitated their reflective process during
retrospective meetings; also, they reported that EmoVizPhy helped them recall specific experiences
or emotions, leading to more meaningful post-it notes. The professional developer stated: “The
visualization of peaks helped me identify problems to be discussed during the retrospective meetings.
For example, it helped me realize that I should avoid doing a merge before a demo. Overall, the data
visualization was useful” (P3). Conversely, four participants (two students and two professional
developers) provided negative feedback on this topic, reporting episodes in which the visualization
of emotional data failed to enhance the reflective process during retrospective meetings. One reason
for this was the lack of notes written during the sprint that could have helped them recall relevant
episodes associated with EDA peaks; a professional developer mentioned: “Maybe, if I had paid
more attention to writing notes in the self-reports, I could have better linked the moments when I was
more agitated with the peaks in the visualization and written more post-it notes accordingly” (P1).
Another reason reported by professional developers was the short, 1-week duration of the sprint.
In such a brief time frame, they felt they could have recalled all the relevant emotional episodes
anyway, even without the help of the tool.
The codeImproved actions proposaladdresses participants’ views on the usefulness of EmoVizPhy
in suggesting process improvement actions during retrospective meetings. Two students offered
positive feedback on this topic. For instance, S5 recalled: “Yes, thanks to the tool we identified a ‘stop’
point: we had to stop causing anxiety to each other” (S5). Conversely, one student and one professional
developer reported that EmoVizPhy did not aid in defining process improvement actions.
The codeImproved emotional awarenessreflects participants’ assessments of whether visualizing
emotional data through EmoVizPhy helped them gain new insights about themselves and improve
their emotional awareness, particularly concerning emotions experienced during the sprint. Eight
participants (seven students and one professional developer) reported positive feedback on this
subject. For instance, one of the students shared: “I’ve noticed that, at the beginning of the day, the
values of EDA are low, which is quite normal; but then they increase above the average after about half
an hour. So the more work, the more stressed I become...” (S5). In contrast, three student participants
felt that EmoVizPhy could not improve their emotional awareness, as exemplified by this comment:
“While the visualization tool was interesting to look at, it didn’t provide any significant insight about
my emotional patterns” (S10).
All the three professional developers participating in the focus group recommendedPromising
use casesfor EmoVizPhy. In particular, they envisioned using the tool to support the onboarding
of new team members—especially those unfamiliar with agile practices. As put by P3 during the
focus group: “I think it could be useful for onboarding developers because it could help new members
understand the agile dynamics.” Furthermore, they encouraged replicating the self-monitoring
protocol in projects with longer sprints, as people tend to forget their emotional experiences more
easily over time; in the words of P3: “For longer sprints—even of two weeks—it can be more helpful
because it might aid in remembering more things occurred over the weeks” (P3).
Finally, the codeDesire to keep monitoring emotionsreflects the inclination of nearly all the
students, except S2, to continue emotional self-monitoring as a means to foster personal growth and
enhance team dynamics. For example, one of them stated: “Yes, I would use this tool in other meetings
because it’s been very interesting understanding mood and emotions of others while working” (S7).


Self-monitoring of Developers’ Emotions 164:23

```
Table 4. Taxonomy for the ThemeInstrumentationUX
```
```
Codes S P
UX of the wristband
Positive feedback S1, S2, S3, S4, S5, S6, S7, S8, S9, S10 -
Negative feedback - P2, P3
UX of the self-reporting tool Positive feedbackNegative feedback S1, S2, S3, S4, S6, S10S1, S4, S6, S8, S9 P1, P2, P3P2
```
```
UX of EmoVizPhy
Positive feedback S2, S3, S5, S6, S7, S10 -
Negative feedback S2, S6, S8, S10 P3
Recommendations for improvement S1, S2, S3, S4, S6, S8, S9 P2
The codes are the result of the qualitative analysis of the interview and focus group transcripts. For each code, the table
lists the participants who shared related excerpts, divided into two groups: students (S) and professional developers (P).
```
```
In Summary. While only a couple of students reported increased focus and productivity as an
unexpected benefit, the tool’s impact on card writing and actions proposal was split evenly
between positive and negative feedback. Most participants reported improved emotional
awareness through the visualization tool, though three found it ineffective. Professional
developers suggested promising use cases, particularly for onboarding new team members
and in projects with longer sprints where emotional recall becomes challenging. Nearly all
students expressed interest in continuing emotion self-monitoring.
```
4.3 Instrumentation UX

In addition to the themes directly addressing our RQ, our thematic analysis revealed an emergent
theme concerning the UX of the instrumentation employed in this study. In Table4, we report the
three codes encompassed by this theme:UX of the wristband,UX of the self-reporting tool, andUX
of EmoVizPhy. Also in this case, we defined sub-codes to distinguish between positive and negative
feedback.
The codeUX of the Wristbandrefers to the participants’ experience with Empatica E4. All students
expressed positive feedback about the wristband, which they found pleasant to wear and easy to
use, as exemplified by this comment: “I found the wristband quite comfortable to wear and I didn’t
have any problems with it” (S1). Conversely, a couple of professional developers reported negative
feedback for two main reasons. First, they found it inconvenient having to remove their personal
smartwatches to wear Empatica E4. For instance, one of them stated: “Sometimes it bothered me,
mainly because I would forget about it. I usually wear a watch on my left wrist, so having to swap it
for another device didn’t come naturally to me” (P3). Second, they perceived the contact with the
plastic material of the wristband as uncomfortable, especially in hot weather. In the words of P1:
“Actually, sometimes it did [bother me], especially when it got very hot. The plastic material made it
uncomfortable to wear [...]” (P1).
TheUX of the self-reporting toolreceived mixed feedback, with negative comments outnumbering
positive ones: six students and all three professionals expressed criticism, while five students and
one professional developer offered favorable comments. Interestingly, four participants (S4, S6, S1,
and P2) shared both positive and negative thoughts.
In particular, participants praised the journaling aspect of the popup application as it prompted
them to regularly reflect on their emotions. Also, one of the practitioners benefited from it as an
activity tracking system: “Actually [the self-reporting tool] was useful to keep track of my activities”
(P1). However, several participants raised concerns about the frequency of the popup appearances.
These were found especially annoying as they repeatedly interrupted work activities. For instance,


164:24 D. Grassi et al.

one of the professional developers remarked: “The popup application was quite annoying for me as
it appeared too often. When I was focused on my workflow, doing various tasks, the popup was very
distracting. So this popup feature could end up being counterproductive” (P3).
On the other hand, theUX of EmoVizPhyelicited a relatively balanced mix of positive and negative
feedback. Six students reported positive experiences, while four students and one professional
developer noted negative aspects, with three students providing both positive and negative feedback.
Participants acknowledged clear presentation of data trends over time and being able to learn
interesting insights into their emotional state. However, participants also reported challenges,
particularly in interpreting the biometric signals —as already discussed in Section4.2. For example,
one participant stated: “The visualization tool worked effectively and was easy to understand. However,
I didn’t know how to interpret the biometric signals, and I think it would be helpful to have highlighted
the most relevant peak in a session” (S3).
Finally, the codeRecommendations for improvementencompasses the various suggestions we
received from the study participants—seven students and one professional developer—aimed at
enhancing different aspects of our experimental setup. Key recommendations revolved around
providing more contextualized insights, such as reporting aggregated emotional data in correlation
with specific causes or activities (e.g., meetings). One of the students articulated: “I would like to
see a summary of the biometric data, such as the average HR and EDA, along with a summary of the
emotions I experienced during the sprint. For example, I’d like to see that, over ten days, I felt stressed
during specific intervals of time” (S4).

```
In Summary. While Empatica E4 was comfortable for students, professionals mostly found
it inconvenient due to conflicts with personal smartwatches and material discomfort in hot
weather. The self-reporting tool drew criticism due to its frequent interruptions, though
some three students participants and one professional developer valued its journaling and
activity tracking capabilities. The EmoVizPhy visualization tool received balanced feedback,
with six students reporting positive experiences and four students plus one professional
developer highlighting challenges, particularly in interpreting biometric signals. Seven
students and one professional developer recommended enhancing it by offering more
contextualized insights related to specific work activities.
```
4.4 Survey Responses

As discussed in Section3, while conducting the semi-structured interviews, we asked participants
to respond to six of the questions using a 4-point ordinal scale and then elaborate freely on their
responses. In this section, we report on the quantitative data collected through the ordinal-scale
items in our interview guide. These ratings offer a complementary perspective, independent of
the authors’ interpretation, on the prevalence of positive and negative feedback across different
aspects of the study.
Figure7 shows the students’ responses. Regarding the UX of the experimental setup, the majority
were not bothered by the wristband (eight responded “never,” and one responded “seldom”).
However, opinions were divided on the popup application. While six students reported being
“never” or “seldom” bothered by it, three were bothered “some of the time,” and one “most of
the time.” Most participants admitted to skipping the popup some of the time (five) or most of
the time (two). Only three students seldom skipped it, and none always filled out the self-report
when prompted to do so. Regarding the participants’ ability to link specific sprint events with the
biometrics displayed in EmoVizPhy, students provided mostly positive feedback (see Figure7). All


Self-monitoring of Developers’ Emotions 164:25

```
Fig. 7. Student responses to the questionnaire administered during the interview.
```
```
Fig. 8. Professional developers’ responses to the questionnaire administered during the interview.
```
of them could associate their experiences with EDA signal peaks, with six students stating “Most of
the time” and four “Some of the time.” Associations with the HR signal were slightly less positive,
as only one student responded “Never,” seven “Some of the time,” and two “Most of the time.” For
self-reports, one student answered “Seldom,” four “Some of the time,” and five “Most of the time.”
Looking at the responses provided by the professional developers (see Figure8), one main
difference emerges: all of the respondents were bothered by wearing the wristband. Moreover,
professional developers shared mixed responses about biometric signals. One developer observed
links with the EDA peaks “Seldom,” while the other two observed them “Some of the time.” HR
associations were “Never” observed by two professional developers, while one observed them
“Some of the time.” Conversely, self-report associations with specific events were more frequent,
with two developers answering “Some of the time,” and one “Most of the time.”

```
In Summary. Based on the quantitative analysis of the ordinal-scale items, students generally
reported that the wristband was unobtrusive, while professional developers found it more
intrusive. The popup application received mixed responses from students, who often skipped
it, while no professional explicitly highlighted it as problematic. Regarding EmoVizPhy,
most students were able to relate sprint events to EDA peaks and, to a slightly lesser
extent, to HR and self-reports. Professional developers, on the other hand, reported fewer
associations with biometric signals, though they more frequently linked events to their
self-reports.
```

164:26 D. Grassi et al.

5 Discussion

The results of our analysis provide insights into the potential of self-monitoring to enhance the
effectiveness of agile retrospective meetings. Students and professional developers provided mixed
feedback on the proposed approach. The findings suggest that self-monitoring offers greater
benefits for novice developers, while experienced professionals perceive it as less valuable to their
retrospective practices. In the following, we answer our RQ by discussing the main takeaway
messages of this study and the associated implications for research and practice.

Toward Supporting Emotional Awareness in Agile Retrospective Meetings. Overall, the findings
suggest that the effectiveness of self-monitoring emotional states during development activities
in enhancing retrospective meetings may vary depending on the developers’ experience, their
familiarity with agile practices, and the longevity of the team. Our study revealed a notable distinc-
tion between student and professional developer participants in both the impact of the proposed
self-monitoring approach on meeting outcomes and the participants’ reception of the method.
Regarding meeting outcomes, we observed a slight increase in the experimental condition in which
EmoVizPhy was used, in both the number of cards contributed and corrective actions proposed
across both participant groups. However, a more detailed analysis of the proposed actions reveals
an interesting difference. Student participants nearly doubled their corrective actions addressing
social and interpersonal dynamics—specifically those categorized as “People/Relationships”—in-
creasing from five actions in control sprints to nine in experimental sprints. In contrast, professional
developers proposed no corrective actions in this category during either experimental sprint. This
disparity suggests that, despite using EmoVizPhy, professional developers either did not identify
relational issues during their retrospectives or deemed such issues insignificant enough to warrant
corrective action.
This evidence can also be interpreted in light of the Tuckman’s model [82], which describes team
formation and development through five stages presenting unique challenges and opportunities
that retrospective meetings can address systematically. In our study, the students’ teams joined
the study after Sprint 0, according to the course calendar, which mostly focused on team forming
and setup of roles. Then, they joined the study during their Sprints 1 and 2, thus likely addressing
the challenges of thestormingandnorming. During these two stages, frustration or disagreements
about goals, expectations, roles, and responsibilities are usually expressed during the retrospectives.
The focus is on conflict resolution to speed up the technical project activities and facilitate the
transition to the norming stage, in which retrospective meetings help consolidate emerging team
cohesion and establish sustainable working practices. This likely explains why the students, who are
less familiar with the agile process and whose teams were just formed, might have benefited most
from the practices of recalling memories associated to emotion-triggering events to be discussed in
the retrospectives. The focus on the “People/Relationships” theme also aligns with the Tuckman’s
vision of the challenges addressed during these early stages of team development. Conversely, the
practitioners were familiar with the agile practices and were part of a consolidated team, i.e., they
were in theperformingstage of the Tuckman’s model. This likely explains why their discussion
on corrective actions focused more on process improvement with less emphasis on interpersonal
relationship.
The qualitative data analysis confirms that student participants perceived our approach as
beneficial for retrospective meetings, reporting most positive feedback concerning improvements
in card writing, action proposal, and emotional awareness. In contrast, only one professional
developer offered encouraging feedback in a couple of instances. In particular, most students
found the visualization of emotional data through EmoVizPhy helpful to gain new insights about
themselves and improve their emotional awareness. The improved focus on relational issues in


Self-monitoring of Developers’ Emotions 164:27

their retrospectives is in line with previous studies emphasizing the importance of awareness and
consideration of emotional states in retrospectives [47], including work by El-Migid et al. [15]
that demonstrated the utility of Emotimonitor for capturing team members’ emotional reactions
to technical tasks through self-report. In addition to this, our results show that all professional
developers and the majority of the students were willing to share their emotions with colleagues
during retrospective meetings. To foster this positive attitude—a crucial ingredient for both team
members’ well-being and overall group productivity—it is essential to cultivate an environment of
psychological safety within the team. Indeed, when team members feel psychologically safe, they
are more likely to open up about challenging or sensitive topics [2].

Greater Perceived Value of Self-monitoring of Emotions for Novice Developers. Most of the students
involved in our study perceived greater value in self-monitoring of emotions than the professional
developers. Specifically, they felt that such practice facilitated their reflective process during retro-
spectives, helping recall specific experiences or emotions and, therefore, provide more meaningful
contributions during the meetings. This effect may stem from the students’ limited experience with
agile processes and retrospectives. By helping them structure their thoughts around emotions,
EmoVizPhy likely supported their learning of this agile practice. This suggests that EmoVizPhy can
help newcomers integrate by fostering emotion self-reflection and sharing with the team. This also
aligns with research emphasizing the importance of retrospective meetings for newcomers [8, 37].

Greater Perceived Value of Self-monitoring of Emotions in Extended Sprints. Overall, the pro-
fessional developers involved in our study experienced limited benefit from the self-monitoring
protocol. They noted that the short sprint duration in their project made it easy to remember
emotionally impactful events from the week, even without self-reports and biometrics. In contrast,
students working in longer, 2-week sprints found the self-monitoring practice much more valuable.
EmoVizPhy helped them recall various triggers for emotional episodes, which they found useful for
discussion during retrospective meetings. Over 2 weeks, specific events and emotional episodes are
harder to recall, making the tool more beneficial for extended sprints. However, this finding requires
further validation with more professional developers who have extensive agile experience. Indeed,
as stated above, the students’ perceived benefit might be influenced by their lack of experience
with agile methodologies and sharing emotions in retrospective meetings.

Need to Balance Contextual Richness and Self-report Intrusiveness. As for the emotion monitoring
protocols proposed in this study, the collection of biometric data via a wearable device did not
pose significant problems. All student participants perceived the wristband as comfortable and
non-invasive. The only critiques, put forward by a couple of professional developers, concern the
need to temporarily replace their smartwatches with Empatica E4 and the inconvenience of wearing
the plastic wristband in hot weather. However, both issues are related to the particular equipment
adopted in this study and will be easily addressed in future work: with the fast-paced advancement
of the wearable technologies, we anticipate being soon able to gather reliable biometric signals
through the sensors available on consumer smartwatches, which users already find appealing and
comfortable to wear.
On a different note, all professional developers and the majority of students considered the
popup application annoying and disruptive—as it repeatedly interrupted their work—suggesting
that more seamless approaches to emotion self-monitoring should be preferred. In contrast, some
participants (including one of the professional developers) pointed out that the notes taken in
the popup form significantly helped them recall emotional episodes associated with self-reported
emotions and biometric data. This evidence highlights the importance of journaling as a practice for
self-awareness, in line with findings from psychological research [78]. Therefore, the open challenge


164:28 D. Grassi et al.

would be to identify an optimal tradeoff, minimizing the intrusiveness of methods used to gather
notes and other contextual information from practitioners. On the one hand, future work could
focus on improving the popup application to prompt developers only when they are not focused on
a particular task. To this aim, they might incorporate strategies emerged in the research on software
developers’ interruptibility, ensuring prompts occur at the best times to complete the self-report
form [92]. On the other hand, follow-up investigations may explore complementing biometrics with
contextual information gathered from other sources, such as calendars and task-tracking systems.
Indeed, recent studies [45, 58, 77, 92] have shown that combining biometrics with contextual data
can provide a more comprehensive understanding of developers’ emotional states and their causes,
ultimately helping them discover significant emotional patterns.

Ethical Considerations. The potential for misuse of behavior monitoring technologies is a concern
we acknowledge. While we do not advocate for implementing monitoring systems that could
trigger privacy concerns, we do support the use of sensor-based emotion monitoring integrated
with self-reporting for developers to gain self-awareness of their own emotions while at work.
In the use case we envision, the information obtained through emotion visualization tools, such
as EmoVizPhy, is acquired individually and can be shared with colleagues only on a voluntary
basis. It is the case of the agile development retrospective meetings, which we investigate in the
current study. As clarified in Section3.2, the access to the emotional feedback based on EmoVizPhy
is done individually by each developerbeforeentering the retrospective meeting (see Figure5),
thus mitigating concerns associated with potential misuse of the biometric information by the
employer, who does not access this data. Further concerns relate to the risks associated with the
misrepresentation of emotions or the misrepresentation of emotional feedback provided by the tool.
EmoVizPhy offers the visualization of notes self-reported by the developers in combination with raw
data collected by the EDA and HR sensors. On the one hand, this offers the possibility of triangulating
subjective self-reported information with objective measures of biometric parameters that are
associated with emotional episodes. However, despite rich literature supporting this association of
biometrics with emotions, we acknowledge that there is a risk of incorrect interpretation by the
developers which might be using the tool without appropriate guidelines for interpretation. We
recognize this limitation and understand that misinterpreting emotions could result in users losing
confidence in the tool ability to serve their emotion awareness goals. However, the impact of such
misclassifications is primarily limited to this loss of user confidence in the tool.

6 Limitations and Tradeoffs

In the following, we discuss the threats to validity of this study. In doing so, we will explain the
rationale behind our methodological choices and how we address the tradeoffs associated with the
decision points, in line with recommendations by Robillard et al. [72].
One of the main limitations associated with the study of emotions in software development is
the risk of threats to construct validity associated with the choices of the instruments for emotion
monitoring as well as the reliability of our measures in capturing the developers’ feelings. This
concern is further enhanced by thein situnature of the data collection protocol. In fact, both
the students and the professional developers operated in their natural setting, i.e., while working
from home on their capstone project and in their workplace, respectively. As for the biometrics, a
tradeoff exists between the need for precision in the collection of raw sensors’ data and the sensors’
invasiveness. In this study, we employed low-cost, lightweight sensors that are comfortable to wear
while working, in line with previous research on biometrics in software development [26, 63]. This
might have lowered the quality of biometrics data collected by the sensors with respect to those
collected in a controlled setting as in previous lab studies from the affective computing domain,


Self-monitoring of Developers’ Emotions 164:29

where a richer sensor setting was enabled with more invasive sensors [24]. On the other hand, the
use of lightweight sensors ensures a higher ecological validity by reducing the risk of inducing
negative emotions that might arise when sensors are uncomfortable to wear, thus introducing a
confounding factor.
Beyond biometrics, we relied on self-reported emotions as collected through our popup appli-
cation. We decided to use self-reported emotions, in terms of valence, arousal, and dominance
scores, along with notes explaining the causes for the reported emotions. Since the goal of this
study is to foster self-reflection, toward the final goal of supporting emotional awareness, we
considered it appropriate to ask participants to self-report their emotions while working on their
development tasks. An alternative to self-reporting would have been to use telemetry, for example
by instrumenting the participants’ computers with activity trackers instead of relying on their
self-reported notes, or by analyzing the emotional valence associated with their facial expression
analysis using state-of-the-art tools, as done by previous work using facial emotion recognition
[67]. We considered the level of invasiveness associated with the use of a webcam to record facial
expressions or with an activity tracker to keep track of the tasks. The tradeoff is privacy vs. more
details about emotions and activities performed during the sprint. An approach based on telemetry
would provide us with richer information, e.g., regarding emotions, based on the outcome of the
facial expression analysis tools [67]. However, such an approach could be perceived as more invasive
and could eventually influence the participants’ behavior. Conversely, self-report is based on the
voluntary self-assessment and journaling of developers to self-assessed feelings and associated
causes, using a sampling approach. Beyond being less invasive, this approach is also more consistent
with our vision of designing and implementing tools and practices that encourage self-reflection and
finally lead to increased emotional awareness. Nevertheless, self-reporting involves interrupting
developers during their work, which may trigger negative emotions and affect the results. As such,
collecting data through self-report eventually results in fewer data points than using telemetry.
However, this does not conflict with our research goal. In fact, in the context of theMad, Sad,
Gladretrospective meetings, identifying the most important emotional episodes associated with
problems or successful events is definitely more valuable than looking at all the episodes occurring
during the sprints.
As for the comparison between control and experimental conditions in the quantitative analysis,
we acknowledge limitations in our statistical analysis due to the small number of data points
collected. While we conducted a comparative analysis examining metrics such as the number of
cards written and actions proposed during retrospective meetings, the limited sample size prevents
us from drawing statistically significant conclusions. Additionally, it is important to note that
several potential confounding factors could explain the quantitative results independent of our
intervention. For professional developers, their established working relationships from previous
sprint collaborations, combined with the possibility of particularly challenging sprints involving
significant technical roadblocks, could have influenced both emotional experiences and retrospective
outcomes. Similarly, the students’ inexperience with agile practices may have created learning effects
that influenced their contributions over time, regardless of the self-monitoring tools. Nevertheless,
the qualitative insights and preliminary quantitative trends we observed provide valuable directional
evidence that warrants further investigation with larger sample sizes in future studies.
As for the pool of participants involved in the study, the choice of recruitment strategies might
introduce threats to external validity, which relate to the generalizability of the results of the
present study and to the participants’ representativeness of agile practice adopted by developers in
a real-life setting. The decision point here is determining where the population of participants shall
be recruited. While being more representative of the software developers population, recruiting
professionals is challenging [17, 80]. A viable and broadly adopted approach is recruiting students


164:30 D. Grassi et al.

through our university channels. We decided to recruit both developers by leveraging our contact
network and students from our undergrad Software Engineering courses. The rationale for this
choice can be explained also in terms of the better representativeness of a more diverse pool of
participants: by considering only students, we would have missed the perspective of experienced
professional developers who are already familiar with agile development and the practice of
retrospective meetings. On the other hand, by considering only professional developers we would
have missed the opportunity to enable a controlled setting with students at their first experience
with agile development. This offers the unique opportunity of eliciting feedback on the usefulness
of the tool in a setting in which team members are not familiar with retrospective meetings. As a
final consideration, both students and professional developers are recruited among volunteers with
an interest in the goal of the study, which might positively influence trust and rigor in adhering
to the study protocol, thus increasing the study’s internal validity. Nevertheless, we acknowledge
that the recruitment of participants among volunteers might introduce a selection bias eventually
leading to a more positive evaluation of the tool on developers’ attitudes. However, looking at our
empirical findings, we notice that we were able to elicit both positive and negative feedback, which
makes us confident of the good ecological validity of the study.
Finally, concerns may arise regarding the use of self-report for the investigation of the emotional
self-awareness and how this is enhanced through the use of EmoVizPhy. This concern is mitigated
by the fact that self-reporting is a consolidated practice in psychological studies investigating
emotional self-awareness. See, for example, the study by Kauer [42] investigating the link between
emotional self-awareness and depressive symptoms. The study demonstrates how self-monitoring
significantly increased emotional self-awareness using self-report as an approach to collect empirical
evidence.

7 Related Work

In the following, we highlight the contributions of our study in the scope of relevant related work
on supporting the emotional awareness of software developers.
Early recognition of emotions, especially negative ones such as frustration [18] and anger [22],
as well as identification of stress-related episodes [36], is crucial to enable just-in-time corrective
actions for developers and team managers to enhance the developers’ well-being and productivity.
To this aim, researchers have proposed tools to visualize emotional trends and dynamics. Vivian
et al. [83] introduced a dashboard that conveys information about team role distribution and emo-
tional states. It offers, both, the team and the individual perspectives, utilizing line and radar charts
for visualization. Similarly, Neupane et al. [66] created a prototype tool capable of automatically
gathering communication records from project teams, identifying emotions and their intensities
using state of art NLP techniques, modeling them into time series, and providing data management.
McDuff et al. [58] developed AffectAura to log audio, visual, physiological, and contextual data
related to users’ workday activities (such as desktop activities, meetings, and locations) and predict
users’ affective states using a classification scheme. When presenting the data using AffectAura,
participants were able to self-reflect on their affective states and activities and recall the reasons
for their emotional states.
A recent study by Khanna and Aldaeej [43] investigates emotions in online agile retrospectives.
The authors analyzed three recorded online retrospective sessions to capture the range of the
emotions. They found that approval, excitement, and relief were among the most frequent positive
emotions, while disappointment and disapproval were common negative emotions. The study also
noted realization and curiosity as prevalent neutral emotions during retrospectives. They suggest
that recognizing and managing emotions in retrospective meetings can lead to better outcomes
and learning experiences for agile teams.


Self-monitoring of Developers’ Emotions 164:31

In our study, we complement the previous work on emotion monitoring in agile development by
investigating the impact of combining self-report and visualization of biometrics to inform agile
retrospective meetings. Specifically, we build upon the empirical design and findings of two former
studies investigating the role of emotions in agile development [15, 30]. In the first study, El-Migid
et al. [15] designed and implemented Emotimonitor, a Trello extension to collect the emotional
reactions of agile team members concerning technical tasks assigned to them. Emotimonitor enables
emotions to be self-reported on Trello cards using emoji reactions. Their evaluation of the tool
provides evidence that emotional feedback can be used to help team members summarize their
emotional reactions, thus enabling emotion identification as a central part of retrospective meetings.
In our previous work [30], we developed and evaluated EmoVizPhy, an emotion visualization tool
that integrates developers’ self-reported emotions, activities, and biometric data. In this preliminary
study, four students wore the Empatica wristband for 2 weeks during a capstone project agile
sprint. They reported their emotions and activities using a popup application and visualized this
data with EmoVizPhy to understand emotional triggers. The participants found the tool useful for
recalling emotional episodes and enhancing emotional awareness. The integrated visualization
helped inform discussions about the causes of emotions during retrospectives, potentially improving
team productivity and well-being.
The current study replicates and extends our previous work [30] by focusing on both team
and individual perspectives, rather than just individual experiences. Specifically, while our earlier
study involved individual participants, this study involved entire teams to observe and analyze
the collective emotional dynamics. Additionally, in this study, we focused on the self-monitoring
process, enabling developers to actively track and reflect on their emotional and physiological
states. Moreover, different from El-Migid et al. [15], we are not only focusing on the self-reporting
of emotions but also considering the biometric data collected during the sprint to provide a more
comprehensive view of the emotional states during retrospective meetings.

8 Conclusions

This study investigates whether self-monitoring emotions during development activities enhances
agile retrospective meetings. In our investigation, we involved both students and professional
developers. Experimental groups wore a wristband to collect biometric data during work and
self-reported their emotional states at regular intervals through a popup application. At the end of
each sprint, participants attended retrospective meetings and used the EmoVizPhy tool to recall
significant emotional experiences. EmoVizPhy provides visualizations that combine biometric data
from the wristband with the self-reported emotional states.
Our findings suggest that the emotion self-monitoring practice and the related support tools pro-
posed in this study may be particularly beneficial for novice developers—with little-to-no experience
with agile practices, as in the case of students—and new teams for which roles and collaboration
dynamics are still being consolidated. We plan a replication of the study with practitioners to isolate
the impact of emotion self-monitoring on the team formation factor.
Another important aspect emerged in this study is the need to balance the richness of data
collected during the sprint with the intrusiveness of data collection tools. Specifically, participants
found the use of a popup application for self-reporting emotional states to be disruptive and
annoying. This points to a key area for future research, concerned with the development of less
intrusive data collection methods. One approach could be to build self-monitoring tools that prompt
developers at optimal times based on studies of developer interruptibility. Another possibility is
integrating biometrics with contextual data from calendars and task-tracking systems, or exploring
automatic emotion recognition as an alternative to self-reporting.


164:32 D. Grassi et al.

References
[1]Ivana Acocella. 2012. The focus groups in social research: Advantages and disadvantages.Quality & Quantity 46
(2012), 1125–1136.
[2]Adam Alami, Mansooreh Zahedi, and Oliver Krancher. 2023. Antecedents of psychological safety in agile software
development teams.Information and Software Technology162 (2023), 107267.
[3]Yanti Andriyani, Rashina Hoda, and Robert Amor. 2017. Reflection in agile retrospectives. InAgile Processes in Software
Engineering and Extreme Programming. Hubert Baumeister, Horst Lichter, and Matthias Riebisch (Eds.), Springer
International Publishing, Cham, 3–19.
[4]Kent Beck, Mike Beedle, Arie Van Bennekum, Alistair Cockburn, Ward Cunningham, Martin Fowler, James Grenning,
Jim Highsmith, Andrew Hunt, Ron Jeffries, et al. 2001. Manifesto for agile software development. Retrieved from
https://agilemanifesto.org/
[5]Margaret M. Bradley and Peter J. Lang. 1994. Measuring emotion: The self-assessment manikin and the semantic
differential.Journal of Behavior Therapy and Experimental Psychiatry25, 1 (1994), 49–59.DOI:https://doi.org/10.1016/
0005-7916(94)90063-9
[6]Virginia Braun and Victoria Clarke. 2006. Using thematic analysis in psychology.Qualitative Research in Psychology3,
2 (2006), 77.
[7]Anne-Marie Brouwer, Elsbeth Van Dam, Jan B. F. Van Erp, Derek P. Spangler, and Justin R. Brooks. 2018. Improving
real-life estimates of emotion based on heart rate: A perspective on taking metabolic heart rate into account.Frontiers
in Human Neuroscience12 (2018), 284.
[8]Jim Buchan, Stephen G. MacDonell, and Jennifer Yang. 2019. Effective team onboarding in agile software development:
Techniques and goals. In2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement
(ESEM), 1–11.DOI:https://doi.org/10.1109/ESEM.2019.8870189
[9]Nathan Cassee, Andrei Agaronian, Eleni Constantinou, Nicole Novielli, and Alexander Serebrenik. 2024. Transformers
and meta-tokenization in sentiment analysis for software engineering.Empirical Software Engineering29, 4 (2024), 77.
DOI:https://doi.org/10.1007/S10664-024-10468-2
[10]Kevin Chow, Thomas Fritz, Liisa Holsti, Skye Barbic, and Joanna McGrenere. 2023. Feeling stressed and unproductive?
A field evaluation of a therapy-inspired digital intervention for knowledge workers.ACM Transactions on Computer-
Human Interaction31, 1, Article 12 (Nov. 2023), 33 pages.DOI:https://doi.org/10.1145/3609330
[11]Broderick Crawford, Ricardo Soto, Claudio León de la Barra, Kathleen Crawford, and Eduardo Olguín. 2014. The
influence of emotions on productivity in software engineering. InHCI International 2014 - Posters’ Extended Abstracts.
Constantine Stephanidis (Ed.), Springer International Publishing, Cham, 307–310.
[12]Alan R. Dennis, Robert M. Fuller, and Joseph S. Valacich. 2008. Media, tasks, and communication processes: A theory
of media synchronicity.MIS Quarterly32, 3 (Sep. 2008), 575–600.
[13]Esther Derby, Diana Larsen, and Ken Schwaber. 2006.Agile Retrospectives: Making Good Teams Great. Pragmatic
Bookshelf.
[14]Torgeir Dingsøyr, Marius Mikalsen, Anniken Solem, and Kathrine Vestues. 2018. Learning in the large - An exploratory
study of retrospectives in large-scale agile development. InAgile Processes in Software Engineering and Extreme
Programming. Juan Garbajosa, Xiaofeng Wang, and Ademar Aguiar (Eds.), Springer International Publishing, Cham,
191–198.
[15]Mohammed-Amr Abd El-Migid, Damon Cai, Thomas Niven, Jeffrey Vo, Kashumi Madampe, John Grundy, and Rashina
Hoda. 2022. Emotimonitor: A trello power-up to capture and monitor emotions of agile teams.Journal of Systems and
Software186 (2022), 111206.DOI:https://doi.org/10.1016/j.jss.2021.111206
[16]L.-B. Fan, J. A. Blumenthal, L. L. Watkins, and A. Sherwood. 2015. Work and home stress: Associations with anxiety and
depression symptoms.Occupational Medicine65, 2 (Jan. 2015), 110–116.DOI:https://doi.org/10.1093/occmed/kqu181
[17]Robert Feldt, Thomas Zimmermann, Gunnar R. Bergersen, Davide Falessi, Andreas Jedlitschka, Natalia Juristo,
Jürgen Münch, Markku Oivo, Per Runeson, Martin Shepperd, et al. 2018. Four commentaries on the use of students
and professionals in empirical software engineering experiments.Empirical Software Engineering23, 6 (Dec. 2018),
3801–3820.DOI:https://doi.org/10.1007/s10664-018-9655-0
[18]Denae Ford and Chris Parnin. 2015. Exploring causes of frustration for software developers. In8th IEEE/ACM
International Workshop on Cooperative and Human Aspects of Software Engineering (CHASE ’15), 115–116.DOI:
https://doi.org/10.1109/CHASE.2015.19
[19]Alexandra Fountaine and Bonita Sharif. 2017. Emotional awareness in software development: Theory and measurement.
In2017 IEEE/ACM 2nd International Workshop on Emotion Awareness in Software Engineering (SEmotion), 28–31.DOI:
https://doi.org/10.1109/SEmotion.2017.12
[20]Thomas Fritz, Andrew Begel, Sebastian C. Müller, Serap Yigit-Elliott, and Manuela Züger. 2014. Using psycho-
physiological measures to assess task difficulty in software development. In36th International Conference on Software
Engineering (ICSE ’14). ACM, 402–413.DOI:https://doi.org/10.1145/2568225.2568266


Self-monitoring of Developers’ Emotions 164:33

```
[21]Thomas Fritz, Alexander Lill, André N. Meyer, Gail C. Murphy, and Lauren Howe. 2023. Cultivating a team mindset
about productivity with a nudge: A field study in hybrid development teams.Proceedings of the ACM on Human-
Computer Interaction7, CSCW2, Article 335 (Oct. 2023), 21 pages.DOI:https://doi.org/10.1145/3610184
[22]Daviti Gachechiladze, Filippo Lanubile, Nicole Novielli, and Alexander Serebrenik. 2017. Anger and its direction in
collaborative software development. In2017 IEEE/ACM 39th International Conference on Software Engineering: New
Ideas and Emerging Technologies Results Track (ICSE-NIER), 11–14.DOI:https://doi.org/10.1109/ICSE-NIER.2017.18
[23]Shadi Ghiasi, Alberto Greco, Riccardo Barbieri, Enzo Pasquale Scilingo, and Gaetano Valenza. 2020. Assessing
autonomic function from electrodermal activity and heart rate variability during cold-pressor test and emotional
challenge.Scientific Reports10, 1 (2020), 5406.
[24]Daniela Girardi, Filippo Lanubile, and Nicole Novielli. 2017. Emotion detection using noninvasive low cost sensors. In
7 th International Conference on Affective Computing and Intelligent Interaction, 125–130.DOI:https://doi.org/10.
1109/ACII.2017.8273589
[25]Daniela Girardi, F. Lanubile, N. Novielli, and D. Fucci. 2018. Sensing developers’ emotions: The design of a replicated
experiment. In2018 IEEE/ACM 3rd International Workshop on Emotion Awareness in Software Engineering (SEmotion),
51–54.DOI:https://doi.org/10.1145/3194932.3194940
[26]Daniela Girardi, Filippo Lanubile, Nicole Novielli, and Alexander Serebrenik. Emotions and perceived productivity of
software developers at the workplace.IEEE Transactions on Software Engineering48, 9 (Sep. 2022), 3326–3341.DOI:
https://doi.org/10.1109/TSE.2021.3087906
[27]Daniela Girardi, Nicole Novielli, Davide Fucci, and Filippo Lanubile. 2020. Recognizing developers’ emotions while
programming. In42nd International Conference on Software Engineering (ICSE ’20), 666–677.DOI:https://doi.org/10.
1145/3377811.3380374
[28]Gerald Glick, Eugene Braunwald, and Robert M. Lewis. 1965. Relative roles of the sympathetic and parasympathetic
nervous systems in the reflex control of heart rate.Circulation Research16, 4 (1965), 363–375.
[29]Luis Gonçalves and Ben Linders. 2015.Getting Value out of Agile Retrospectives: A Toolbox of Retrospective Exercises.
Ben Linders Publishing.
[30]Daniela Grassi, Filippo Lanubile, Nicole Novielli, and Alexander Serebrenik. 2023. Towards supporting emotion
awareness in retrospective meetings. In2023 IEEE/ACM 45th International Conference on Software Engineering:
New Ideas and Emerging Results (ICSE-NIER). IEEE Computer Society, 101–105.DOI:https://doi.org/10.1109/ICSE-
NIER58687.2023.00024
[31]Daniel Graziotin, Fabian Fagerholm, Xiaofeng Wang, and Pekka Abrahamsson. 2017. On the unhappiness of software
developers. In21st International Conference on Evaluation and Assessment in Software Engineering (EASE ’17).DOI:https:
//doi.org/https://doi.org/10.1145/3084226.3084242
[32]Daniel Graziotin, Fabian Fagerholm, Xiaofeng Wang, and Pekka Abrahamsson. 2018. What happens when software
developers are (un)happy.Journal of Systems and Software140 (2018), 32–47.DOI:https://doi.org/10.1016/j.jss.2018.
02.041
[33]Daniel Graziotin, Xiaofeng Wang, and Pekka Abrahamsson. 2013. Are happy developers more productive? The
correlation of affective states of software developers and their self-assessed productivity. InInternational Conference
on Product Focused Software Process Improvement, 50–64.DOI:https://doi.org/10.1007/978-3-642-39259-7_7
[34]Daniel Graziotin, Xiaofeng Wang, and Pekka Abrahamsson. 2014. Happy software developers solve problems better:
Psychological measurements in empirical software engineering.PeerJ2 (2014), e289.
[35]Daniel Graziotin, Xiaofeng Wang, and Pekka Abrahamsson. 2015. Do feelings matter? On the correlation of affects
and the self-assessed productivity in software engineering.Journal of Software: Evolution and Process27, 7 (2015),
467–487.DOI:https://doi.org/10.1002/smr.1673
[36]Isabella Graßl, Gordon Fraser, Stefan Trieflinger, and Marco Kuhrmann. 2023. Exposing software engineering students
to stressful projects: Does diversity matter? In2023 IEEE/ACM 45th International Conference on Software Engineering:
Software Engineering Education and Training (ICSE-SEET). IEEE Computer Society, 210–222.DOI:https://doi.org/10.
1109/ICSE-SEET58685.2023.00026
[37]Peggy Gregory, Diane E. Strode, Helen Sharp, and Leonor Barroca. 2022. An onboarding model for integrating
newcomers into agile project teams.Information and Software Technology143 (2022), 106792.DOI:https://doi.org/10.
1016/j.infsof.2021.106792
[38]Emitza Guzman and Bernd Bruegge. 2013. Towards emotional awareness in software development teams. InJoint
Meeting of the European Software Engineering Conference and the ACM SIGSOFT Symposium on the Foundations of
Software Engineering (ESEC/FSE ’13), 671–674.DOI:https://doi.org/10.1145/2491411.2494578
[39]Emitza Guzman and Walid Maalej. 2014. How do users like this feature? A fine grained sentiment analysis of
app reviews. In2014 IEEE 22nd Internatonal Requirements Engineering Conference (RE). IEEE, 153–162.DOI:https:
//doi.org/10.1109/RE.2014.6912257
```

164:34 D. Grassi et al.

```
[40]Andreas Holzinger, Manuel Bruschi, and Wolfgang Eder. 2013. On interactive data visualization of physiological
low-cost-sensor data with focus on mental stress. InAvailability, Reliability, and Security in Information Systems
and HCI. Alfredo Cuzzocrea, Christian Kittl, Dimitris E. Simos, Edgar Weippl, and Lida Xu (Eds.), Springer Berlin
Heidelberg, Berlin, Heidelberg, 469–480.
[41]P. J. Jordan and N. M. Ashkanasy. 2006.Emotional Intelligence, Emotional Self-Awareness, and Team Effectiveness.
Lawrence Erlbaum Associates Publishers, 145–163.DOI:https://doi.org/10.4324/9780203763896
[42]Sylvia D. Kauer. 2012. Emotional Self-Awareness and Depressive Symptoms: An Investigation of an
Early Intervention Mobile Phone Self-Monitoring Program for Adolescents. PhD thesis, School of Psy-
chological Science, The University of Melbourne. Retrieved from https://citeseerx.ist.psu.edu/docu-
ment?repid=rep1&type=pdf&doi=1fe328cceb9caa6b829c826be6250a3ab58cf988
[43]Dron Khanna and Abdullah Aldaeej. 2024. Exploring emotions in online team meetings: Unpacking agile retrospective.
InSoftware Business. Sami Hyrynsalmi, Jürgen Münch, Kari Smolander, and Jorge Melegati (Eds.), Springer Nature
Switzerland, Cham, 416–424.
[44]Jonghwa Kim and Elisabeth André. 2008. Emotion recognition based on physiological changes in music listening.
IEEE Transactions on Pattern Analysis and Machine Intelligence30, 12 (2008), 2067–2083.DOI:https://doi.org/10.1109/
TPAMI.2008.26
[45]Rafal Kocielnik, Natalia Sidorova, Fabrizio Maria Maggi, Martin Ouwerkerk, and Joyce H. D. M. Westerink. 2013.
Smart technologies for long-term stress monitoring at work. In26th IEEE International Symposium on Computer-Based
Medical Systems, 53–58.DOI:https://doi.org/10.1109/CBMS.2013.6627764
[46]Sander Koelstra, Christian Mühl, Mohammad Soleymani, Jong-Seok Lee, Ashkan Yazdani, Touradj Ebrahimi, Thierry
Pun, Anton Nijholt, and Ioannis Patras. 2012. DEAP: A database for emotion analysis using physiological signals.
IEEE Transactions on Affective Computing3, 1 (2012), 18–31.DOI:https://doi.org/10.1109/T-AFFC.2011.15
[47]Fabian Kortum, Jil Klünder, Oliver Karras, Wasja Brunotte, and Kurt Schneider. 2020. Which information help agile
teams the most? An experience report on the problems and needs. In2020 46th Euromicro Conference on Software
Engineering and Advanced Applications (SEAA), 306–313.DOI:https://doi.org/10.1109/SEAA51224.2020.00058
[48]Brigitte M. Kudielka, Angelika Buske-Kirschbaum, Dirk H. Hellhammer, and Clemens Kirschbaum. 2004. Differential
heart rate reactivity and recovery after psychosocial stress (TSST) in healthy children, younger adults, and elderly
adults: The impact of age and gender.International Journal of Behavioral Medicine11 (2004), 116–121.
[49]Miikka Kuutila, Mika Mäntylä, Umar Farooq, and Maëlick Claes. 2019. Time pressure in software engineering:
A systematic literature review.Information and Software Technology121 (May 2020), 106257. DOI: 10.1016/j.inf-
sof.2020.106257
[50]Miikka Kuutila, Mika V. Mäntylä, Maëlick Claes, Marko Elovainio, and Bram Adams. 2018. Using experience sampling
to link software repositories with emotions and work well-being. In12th ACM/IEEE International Symposium on
Empirical Software Engineering and Measurement (ESEM ’18). ACM, New York, NY, Article 29, 10 pages.DOI:https:
//doi.org/10.1145/3239235.3239245
[51]J. Richard Landis and Gary G. Koch. 1977. The measurement of observer agreement for categorical data.Biometrics
33, 1 (1977), 159–174. Retrieved fromhttp://www.jstor.org/stable/2529310
[52]Reed Larson and Mihaly Csikszentmihalyi. 2014.The Experience Sampling. Springer Netherlands, 21–34.DOI:https:
//doi.org/10.1007/978-94-017-9088-8_2
[53]Richard S. Lazarus and Susan Folkman. 1984.Stress, Appraisal, and Coping. Springer Publishing Company.
[54]Bin Lin, Nathan Cassee, Alexander Serebrenik, Gabriele Bavota, Nicole Novielli, and Michele Lanza. 2022. Opinion
mining for software development: A systematic literature review.ACM Transactions on Software Engineering and
Methodology31, 3, Article 38 (Mar. 2022), 41 pages.DOI:https://doi.org/10.1145/3490388
[55]Marc Loeffler. 2017.Improving Agile Retrospectives: helping Teams Become More Efficient. Addison-Wesley Professional.
[56]Kashumi Madampe, Rashina Hoda, and John Grundy. 2023. A framework for emotion-oriented requirements change
handling in agile software engineering.IEEE Transactions on Software Engineering49, 5 (2023), 3325–3343.DOI:
https://doi.org/10.1109/TSE.2023.3253145
[57]Mika Mäntylä, Bram Adams, Giuseppe Destefanis, Daniel Graziotin, and Marco Ortu. 2016. Mining valence, arousal,
and dominance: Possibilities for detecting burnout and productivity? In13th International Conference on Mining
Software Repositories (MSR 2016), 247–258.DOI:https://doi.org/10.1145/2901739.2901752
[58]Daniel McDuff, Amy Karlson, Ashish Kapoor, Asta Roseway, and Mary Czerwinski. 2012. AffectAura: An intelligent
system for emotional memory. InACM Conference on Human Factors in Computing Systems (CHI ’12). ACM, 849–858.
Retrieved fromhttps://www.microsoft.com/en-us/researc/publication/affectaura-an-intelligent-system-for-emotional-
memory/.
[59]J. E. McGrath. 1984.Groups: Interaction and Performance. Prentice-Hall, Englewood Cliffs/N.J.
[60]A. Meyer, E. T. Barr, C. Bird, and T. Zimmermann. 2021. Today was a good day: The daily life of software developers.
IEEE Transactions on Software Engineering47, 5 (May 2021), 863–880. DOI: 10.1109/TSE.2019.2904957
```

Self-monitoring of Developers’ Emotions 164:35

```
[61]André N. Meyer, Gail C. Murphy, Thomas Zimmermann, and Thomas Fritz. 2019. Enabling good work habits in
software developers through reflective goal-setting.IEEE Transactions on Software Engineering47, 9 (2019), 1872–1885.
[62]Alessandra Maciel, Paz Milani, Margaret-Anne Storey, Vivek Katial, and Lauren Peate. 2025. Exploring retrospective
meeting practices and the use of data in agile teams. InThe 18th IEEE/ACM International Conference on Cooperative
and Human Aspects of Software Engineering (CHASE ’25). IEEE Computer Society.
[63]Sebastian C. Müller and Thomas Fritz. 2015. Stuck and frustrated or in flow and happy: Sensing developers’ emotions
and progress. In37th IEEE/ACM International Conference on Software Engineering (ICSE ’15), Volume 1. IEEE Computer
Society, 688–699.DOI:https://doi.org/10.1109/ICSE.2015.334
[64]Alessandro Murgia, Marco Ortu, Parastou Tourani, Bram Adams, and Serge Demeyer. 2018. An exploratory qualitative
and quantitative analysis of emotions in issue report comments of open source systems.Empirical Software Engineering
23, 1 (Feb. 2018), 521–564.DOI:https://doi.org/10.1007/s10664-017-9526-0
[65]Alessandro Murgia, Parastou Tourani, Bram Adams, and Marco Ortu. 2014. Do developers feel emotions? An ex-
ploratory analysis of emotions in software artifacts. In11th Working Conference on Mining Software Repositories (MSR
’14), 262–271.DOI:https://doi.org/10.1145/2597073.2597086
[66]Krishna Prasad Neupane, Kabo Cheung, and Yi Wang. 2019. EmoD: An end-to-end approach for investigating emotion
dynamics in software development. In2019 IEEE International Conference on Software Maintenance and Evolution
(ICSME), 252–256.DOI:https://doi.org/10.1109/ICSME.2019.00038
[67]Nicole Novielli, Daniela Grassi, Filippo Lanubile, and Alexander Serebrenik. 2022. Sensor-Based emotion recognition
in software development: Facial expressions as gold standard. In2022 10th International Conference on Affective
Computing and Intelligent Interaction (ACII), 1–8.DOI:https://doi.org/10.1109/ACII55700.2022.9953808
[68]Nicole Novielli and Alexander Serebrenik. 2023.Emotion Analysis in Software Ecosystems. Springer International
Publishing, Cham, 105–127.DOI:https://doi.org/10.1007/978-3-031-36060-2_5
[69]Martin Obaidi and Jil Klünder. 2021. Development and application of sentiment analysis tools in software engineering:
A systematic literature review. InProceedings of the 25th International Conference on Evaluation and Assessment in
Software Engineering (EASE ’21). ACM, New York, NY, 80–89.DOI:https://doi.org/10.1145/3463274.3463328
[70]Adam Przybyłek and Dagmara Kotecka. 2017. Making agile retrospectives more awesome. In2017 Federated Conference
on Computer Science and Information Systems (FedCSIS), 1211–1216.DOI:https://doi.org/10.15439/2017F423
[71]Tatyana Reinhardt, Christian Schmahl, Stefan Wüst, and Martin Bohus. 2012. Salivary cortisol, heart rate, electrodermal
activity and subjective stress responses to the Mannheim Multicomponent Stress Test (MMST).Psychiatry Research
198, 1 (2012), 106–111.
[72]Martin P. Robillard, Deeksha M. Arya, Neil A. Ernst, Jin L. C. Guo, Maxime Lamothe, Mathieu Nassif, Nicole Novielli,
Alexander Serebrenik, Igor Steinmacher, and Klaas-Jan Stol. 2024. Communicating study design trade-offs in software
engineering.ACM Transactions on Software Engineering and Methodology33, 5, Article 112 (Jun. 2024), 10 pages.DOI:
https://doi.org/10.1145/3649598
[73]James Russell. 1991. Culture and the categorization of emotions.Psychological Bulletin110, 3 (1991), 426–450.DOI:
https://doi.org/10.1037/0033-2909.110.3.426
[74]Anastasia Ruvimova, Alexander Lill, Jan Gugler, Lauren Howe, Elaine Huang, Gail Murphy, and Thomas Fritz. 2022.
An exploratory study of productivity perceptions in software teams. In44th International Conference on Software
Engineering (ICSE ’22). ACM, New York, NY, 99–111.DOI:https://doi.org/10.1145/3510003.3510081
[75]Kurt Schneider, Olga Liskin, Hilko Paulsen, and Simone Kauffeld. 2015. Media, mood, and meetings: Related to
project success?ACM Transactions on Computing Education15, 4, Article 21 (Dec. 2015), 33 pages.DOI:https:
//doi.org/10.1145/2771440
[76]Ken Schwaber and Jeff Sutherland. 2020. The 2020 Scrum Guide. Retrieved fromhttps://scrumguides.org/scrum-
guide.html
[77]Moushumi Sharmin, Andrew Raij, David Epstien, Inbal Nahum-Shani, J. Gayle Beck, Sudip Vhaduri, Kenzie Preston,
and Santosh Kumar. 2015. Visualization of time-series sensor data to inform the design of just-in-time adaptive stress
interventions. In2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp ’15).
ACM, New York, NY, 505–516.DOI:https://doi.org/10.1145/2750858.2807537
[78]Joshua Smyth, Jennifer Johnson, Benjamin Auer, Eric Lehman, Giovanni Talamo, and Christopher Sciamanna. 2018.
Online positive affect journaling in the improvement of mental distress and well-being in general medical patients
with elevated anxiety symptoms: A preliminary randomized controlled trial.JMIR Mental Health5, 4 (2018), e11290.
DOI:https://doi.org/10.2196/11290
[79]Mohammad Soleymani, Sadjad Asghari-Esfeden, Yun Fu, and Maja Pantic. 2016. Analysis of EEG signals and facial
expressions for continuous emotion detection.IEEE Transactions on Affective Computing7, 1 (2016), 17–28.DOI:
https://doi.org/10.1109/TAFFC.2015.2436926
[80]Mohammad Tahaei and Kami Vaniea. 2022. Recruiting participants with programming skills: A comparison of four
crowdsourcing platforms and a CS student mailing list. In2022 CHI Conference on Human Factors in Computing
Systems (CHI ’22). ACM, New York, NY, Article 590, 15 pages.DOI:https://doi.org/10.1145/3491102.3501957
```

```
164:36 D. Grassi et al.
```
```
[81]Sara Taylor, Natasha Jaques, Weixuan Chen, Szymon Fedor, Akane Sano, and Rosalind Picard. 2015. Automatic
identification of artifacts in electrodermal activity data.Conference Proceedings: Annual International Conference of
the IEEE Engineering in Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society, 1934–1937.
DOI:https://doi.org/10.1109/EMBC.2015.7318762
[82]B. W. Tuckman. 1965. Developmental sequence in small groups.Psychological Bulletin63, 6 (1965), 384–399.DOI:
https://doi.org/10.1037/h0022100
[83]Rebecca Vivian, Hamid Tarmazdi, Katrina Falkner, Nickolas Falkner, and Claudia Szabo. 2015. The development of a
dashboard tool for visualising online teamwork discussions. In2015 IEEE/ACM 37th IEEE International Conference on
Software Engineering, Vol. 2, 380–388.DOI:https://doi.org/10.1109/ICSE.2015.170
[84]Hana Vrzakova, Andrew Begel, Lauri Mehtätalo, and Roman Bednarik. 2020. Affect recognition in code review:
An in-situ biometric study of reviewer’s affect.Journal of Systems and Software159 (2020), 110434.DOI:https:
//doi.org/10.1016/j.jss.2019.110434
[85]Wei Wang, John Grundy, Hourieh Khalajzadeh, Anuradha Madugalla, and Humphrey O. Obie. 2025. Designing adaptive
user interfaces for mHealth applications targeting chronic disease: A user-centered approach.ACM Transactions on
Software Engineering and Methodology(April 2025).DOI:https://doi.org/10.1145/3731750
[86]Joyce H. D. M. Westerink, Roos J. E. Rajae-Joordens, Martin Ouwerkerk, Marieke van Dooren, Sam Jelfs, Ad. J. M.
Denissen, Eric Penning de Vries, and Raymond van Ee. 2020. Deriving a cortisol-related stress indicator from wearable
skin conductance measurements: Quantitative model & experimental validation.Frontiers in Computer Science 2
(2020), 39.
[87]Chauncey Wilson. 2014. Semi-structured interviews.Interview Techniques for UX Practitioners1 (2014), 23–41.
[88]Michal R. Wrobel. 2013. Emotions in the software development process. In2013 6th International Conference on Human
System Interactions (HSI), 518–523.DOI:https://doi.org/10.1109/HSI.2013.6577875
[89]Mengru Xue, Rong-Hao Liang, Bin Yu, Mathias Funk, Jun Hu, and Loe Feijs. 2019. AffectiveWall: Designing collective
stress-related physiological data visualization for reflection.IEEE Access7 (2019), 131289–131303.DOI:https://doi.
org/10.1109/ACCESS.2019.2940866
[90]Bin Yu, Mathias Funk, Jun Hu, and Loe Feijs. 2017. StressTree: A metaphorical visualization for biofeedback-assisted
stress management. In2017 Conference on Designing Interactive Systems (DIS ’17). ACM, New York, NY, 333–337.DOI:
https://doi.org/10.1145/3064663.3064729
[91]Bin Yu, Jun Hu, Mathias Funk, Rong-Hao Liang, Mengru Xue, and Loe Feijs. 2018. RESonance: Lightweight, room-scale
audio-visual biofeedback for immersive relaxation training.IEEE Access6 (2018), 38336–38347.
[92]Manuela Züger, S. C. Müller, A. N. Meyer, and T. Fritz. 2018. Sensing interruptibility in the office: A field study on the
use of biometric and computer interaction sensors. In2018 CHI Conference on Human Factors in Computing Systems
(CHI ’18). ACM, 1–14.DOI:https://doi.org/10.1145/3173574.3174165
```
```
Appendices
A Questions for the Semi-Structured Individual Interviews
```
Feedback on the Experiment.

```
(1) Did wearing the wristband bother you?
ÉMost of the time
ÉSome of the time
ÉSeldom
ÉNever
(1a) Why? Can you tell me more about it?
(1b) Would you have preferred another device (a webcam or a watch with other integrated
functions)?
(2) Did answering the popup questions bother you?
ÉMost of the time
ÉSome of the time
ÉSeldom
ÉNever
(2a) In which cases?
```

```
Self-monitoring of Developers’ Emotions 164:37
```
```
(3) Did you ever skip the popup?
ÉMost of the time
ÉSome of the time
ÉSeldom
ÉNever
(3a) Why? Can you tell me more about it?
```
Perceived Usefulness of EmoVizPhy in the Retrospective Meeting.

```
(4)Were you able to associate the peaks of electrodermal activity with specific events during
the sprint?
ÉMost of the time
ÉSome of the time
ÉSeldom
ÉNever
(4a) Can you give me an example of a peak you can associate with a specific event?
(4b) Can you give me an example of a peak you cannot associate with a specific event?
(5) Were you able to associate the HR signal with specific events during the sprint?
ÉMost of the time
ÉSome of the time
ÉSeldom
ÉNever
(5a) Can you give me an example of a peak you can associate with a specific event?
(5b) Can you give me an example of a peak you cannot associate with a specific event?
(6) Were you able to associate the self-report with specific events during the sprint?
ÉMost of the time
ÉSome of the time
ÉSeldom
ÉNever
(6a) Can you give me an example of a self-report you can associate with a specific event?
(6b) Can you give me an example of a self-report you cannot associate with a specific event?
(7) Was the data visualization helpful in writing the notes on the whiteboard during the retro-
spective meeting?
(7a) Can you give me some examples?
(8)Can you please rank the data sources (electrodermal activity, HR, self-report) with respect to
the help provided in writing the notes on the whiteboard?
(9)Were you familiar with any of these data sources (electrodermal activity, HR, self-report)
before taking part in the study?
(10)During the retrospective meeting, did you choose to not disclose any emotions encountered
during the sprint?
(10a) Why?
```
```
B Questions for the Focus Groups
```
Retrospective Meeting Output.


```
164:38 D. Grassi et al.
```
```
(11)Compared to the usual retrospective meeting, was the data visualization helpful in writing
notes on the whiteboard during the retrospective meeting?
(12)Compared to the usual retrospective meeting, was the data visualization helpful in proposing
process improvement actions?
```
Reflection on EmoVizPhy.

```
(13)What features were missing in EmoVizPhy?
(14)How much did you feel that your emotional response data was being handled appropriately
privacy-wise?
(15)How would you rate the appearance of the user interface aesthetic-wise? How would you
improve it?
```
Reflection on Emotion Awareness.

```
(16)Do you think it is useful to be aware of your own emotions at work? Why?
(17)Do you think it is useful to be aware of your peers’ emotions at work? Why?
```
```
Received 2 July 2024; revised 28 August 2025; accepted 2 September 2025
```

