---
title: "Data Architectural Patterns"
draft: true
# description: ""
# date: 2026-04-16
# featureimage: "featured.jpg"
# tags: ["Personal"]
---

<!-- > [!NOTE]
> All thoughts expressed in this Blog Post are my own and don't relfect those of my current, or past employers. -->

<!-- Space for a Quote -->
<!-- {{< typeit
  tag=h4
  speed=80
  lifeLike=true
  breakLines=true
  loop=false
>}}
"Travel isn't always pretty. It isn't always comfortable. Sometimes it hurts, it even breaks your heart. But that's okay. The journey changes you; it should change you. It leaves marks on your memory, on your consciousness, on your heart, and on your body. You take something with you. Hopefully you leave something good behind." - Anthony Bourdain
{{< /typeit >}} -->

---

## Notes

Throughout my time working as a "*Data Person*". I've worked for a few different organisations, operating in different industries with differing levels of data maturity.

However, there are some constant anti-patterns that I notice throughout these companies.

I want to use this article today to try and put into words things that organisations know they suffer from, but don't quite know how to define and describe.

## You don't know what you don't know

Most businesses are very good at operating their business. They know how to:

* sell insurance
* generate electricity
* manage customer relationships

yada yada

But that doesn't necessarily mean they understand how to translate those activities into an information architecture that supports good decision-making.

SME decision makers (*generally the profit centres of business's or people that keep the lights on*), are usually (*but not always*) non-technical, but are generally exceptional at their core competency.

This means they're unable to verbalize their specific requirements, even to experienced BA's. From what I can see however, they still want access to data to help them in their day to day work. **NOTE:** I don't want to phrase this as a failing of BA's, I want to phrase it instead as a translation issue, requirements gathering cannot recover requirements that nobody has yet conceptualised.

### What questions do business's need to ask?

This is where organisations need to take the time to sit down and ask questions:

1) What information do we need to make good decisions through the day / week / year / life. Also, what happens when a decision is made, does it then create a flow-on effect? What other facts, measures and context do we need to inform that decision. How quickly does the information need to be available? What kind of accuracy / completenes must the information be in, and therefore what happens if the information is wrong, missing or late?

2) How do we store this information in a way that scales, allows for easy migration and can support a wide range of analytics activities.

3) How do we figure out ways to expose this information to a wide range of stakeholders ["BA's", "SME's", "Analysts", "Engineers", Scientists"] etc in a way that works with each of their specific use cases.

## New and Shiny

I also notice that there seems to be all encompassing pressure to experiment with the latest in software / data developments. i.e. utilising "AI" / Data Science / LLM's / Agents etc etc.

The problem with this however is that there is very little capacity for people to experiment in their work hours (*consumed by BAU / projects*) as well as the elephant in the room being that very few organisations seem to have the foundations down to try any of the more advanced stuff. i.e. trying to build a sky-scraper with no foundations.

The other part of this as well, is that, because of that pressure I described, it means that some teams / data leaders feel the need to integrate "*shiny new stuff*" without any sort of business valued defined from it? I think this is fine in an experimentation sense, but integrating for the sake of integration is a poor use of business resources.

**NOTE:** I also wanted to know that a succesful, or unsuccesful experiment is just that. It captures states at a point in time, and given the changing nature of the world, these findings / assumptions need to be challenged, and then re-challenged, what worked / didn't work at a point in time, may now have a stronger footing for success / failure in the future.

## Death by Analysis

Another issue that I seem to see quite a lot is death by analysis / dashboard. It's very easy for SME's to come to an analyst / engineer with a question and then, while trying to do their best, the analyst does the analysis, and creates a dashboard, which then enables the SME to self-server in the future.

Good actions here create negative outcomes. Not necessairly at first, in fact, the dashboard might be shown in management or executive meetings (*nice*). However, we now have another artifact that we need to govern, manage, triage, debug. So, the question then becomes, how do we decide what can be a piece of ad-hoc analysis, and what should we build dashboards / more permanent solutions for?

Well a good question to start this off is: "*What is the most economical, reliable way to support this decision over time?*"

I'd personally say it comes down to how often does the SME make the decision that the dashboard / reporting will support. i.e. if he needs to make the decision every single day, then perhaps a dashboard that he can save to his tabs is a strong idea.

However, if the same SME wants to test something, perhaps one off reporting, with a call at the end to explain the findings is stronger. Similarly, if a large number of people keep asking the same question (*or questions*), this is another indicator that a dashboard could be strong solution.

**NOTE:** I'd also challenge one business assumption: dashboards don't always enable self-service. Sometimes they simply relocate the bottleneck. Users may still need an analyst to explain why a number changed, reconcile conflicting figures or interpret an unexpected result.

## Genies should be blue

Natural language to SQL through tooling like Databricks Genies seems to be the hot trend to adopt in 2026, and for good reason. It primarily enables non-technical users to be able to query tables to retrieve answers without the need of a traditional analyst to understand the context of the request and then write the query.

On one hand I'm sad, because it may result in decreased demand and wage compression for traditional analysts, however, on the other hand, it may enable non-technical users (*that are generally closer to actual business decision making and problem solving*) to get answers quicker.

But enough about me, this is a super solid idea, but I want to touch on something I just said "*without the need of a traditional analyst to understand the context of the request and then write the query*". What I'm referring to by "*understand the context of the request*" is that in order to answer a question, you need to be able to understand the world around you. As a individual within a company, as long as you've been working for said company for a sufficient amount of time, as a person, you understand (*roughly, dependent on person*) the business context and the world around you.

The same cannot be said for a LLM. Thus, the creation, management, and upkeep of a defined context layer (*by context layer, I mean a big wall of text that can be fed to a LLM*) is essential to stop LLM's from hallucinating answers, or creating conflicting definitions / metrics.

**NOTE:** it was probably silly to say "*big wall of text that can be fed to a LLM*". a good context layer will have the following:

* Semantic definitions: what things like "revenue", "active customer", "outage" or "completed claim" actually means.
* Relationships and grain: how tables relate to each other, what a row represents, which joins are valid.
* Business rules: exclusions, time periods, calculation logic and exceptional cases.
* Operational context: how the business works, what its processes are, and what assumptions matter when interpreting results.

So to wrap this up, make sure that you have your business definitions and business context layer created, before creating your genie. (*Once again, make sure your foundations are sound before doing the shiny stuff*)

<!-- ## What goes where and mapping -->

<!-- Weak ass section -->
<!-- Generally it's easier to have consistency across the business, but sometimes specific situations call for specific requirements, which call for specific tools. Thus, you end up with different business units using different tools.

This is fine in practice, however, it does mean that you need to have some kind of organisational map to define where (*for example*) the "markets" business unit keeps their core data, where they keep their documentation, where they keep their task management (*jira etc*), and then the same needs to be done with the "customer services" business unit.

People also need to be told where to put stuff, what format to put stuff in, and why. For example, one of the first things I do when starting a project team is creating a space in Sharepoint (*if the business is MS enabled*). Then, I set out a directory structure that hopefully enables users within the team to easily understand where to put specific pieces of text, video, images etc, such that the reposistory can grow into a source of truth, rather than a dumping ground. -->

## Silos and a Lack of consistency

There's also a prevelant issue of siloing and lack of consistency in data-approache across organisataions. i.e. the markets team (*due to the nature of their work*) might operate out of spreadsheets, where as the customer services team has a SASS product for managing their information.

Both of these approaches are ok (*ish*) however, getting organisations working with a consisent set of tools that can be scalable, and changable over time (*don't lock people down or drown them in red tape*).

However, the big issue is that if an executive wants a top-down view of the business, he/she can sometimes find themselves in a data-rabbit hole with 3-5 (*or more*) tabs open, trying to join data themselves and generally just getting frustrated.

My belief in this space is that it doesnt' matter where the data is stored, just that it should be stored in a consisent location, such that competent data-engineers can create expose these views to analysts, to then create simple / refined BI reporting to provide to executives to give them a one stop shop for the information they need.

**NOTE:** A business doesn't necessarily need every dataset physically consolidated into one platform. It needs to be able to discover, access, interpret and combine the information it is authorised to use.

This could involve:

* a central lakehouse
* federated access
* replicated datasets
* APIs

(*or a combination of these approaches.*)

The important architectural requirement is that the data is:

* discoverable
* its meaning is understood
* its lineage is traceable
* its quality is appropriate for the intended use.

## Evaluating external products

It's curious to me how often I see headaches and people reaching for coffee when they talk about a legacy SASS product that's been in the business for many years and how it seems to restrict their access to critical information they need.

i.e. finance information is stored in oracle, however, anyone who's ever worked in oracle knows how much of a pain it is to get data out of oracle for bespoke analytics or reporting.

As such, deep consideration should be placed when deciding to pursue a external solution to a problem, when especially in the age of AI, developing in-house may prove to be the stronger solution.

**NOTE** not necessairly always true, however, defintly something to think about.

## BI Not using Gold Tables

* I'm unsure at how much of a problem it is, but it's for sure an anti-pattern, but I notice a lot of gold tables still aren't BI ready, thus, we have BI analysts / other SME's performing downstream transformations on tables to get them into the format they require for their work.

## Conclusion

1. Translation failures
Business expertise isn't automatically translated into well-defined information requirements, business rules and decision-support systems.

2. Weak foundations
Data models, definitions, integration patterns and governance aren't sufficiently mature to support the complexity being layered on top.

3. Poor resource allocation
Teams are pressured to innovate and deliver permanent solutions without sufficient capacity or evidence that the investment is worthwhile.

4. Organisational fragmentation
Information, definitions, documentation and ownership are scattered across teams, platforms and processes.

5. Lifecycle neglect
Organisations focus on building solutions but insufficiently consider their ongoing maintenance, governance, adoption and eventual retirement.

I'll go further into each of these problems below, but I want to first explain that there is no such thing as perfect, and everyone is doing the best with what they have.

With this too, there isn't a perfect way to do something at each organisation, and almost all decisions come with trade-offs... i.e. Centralisation versus federation, custom development versus SaaS, self-service versus managed reporting, and experimentation versus production readiness are all trade-offs rather than binary choices.

The purpose of data architecture isn't to maximise the number of datasets, pipelines, dashboards or AI tools an organisation possesses. It's to enable people to make better decisions, at an appropriate cost and level of risk.
