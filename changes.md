Points given:

- BrewContent is a new product for the future of Content creation.
- It has features for AI video, voice, image and text generation alongside automating the entire flow.


Simple LLM:

Prompt: Write a 50 word blog for publishing with the following points: {points}

Output:
**BrewContent: The Future of Content Creation**

Meet BrewContent — the future of content creation. This new product packs AI-powered video, voice, image, and text generation into one platform, while automating the entire creation flow. Its comprehensive suite of tools helps creators work smarter, faster, and at scale. BrewContent is where the future of creating begins.


Example based LLM:

Prompt: Write a 50 word blog for publishing. First, make rules based on how this example is written: "
               "{examples}, then, use those rules alongside these humanizing rules to avoid LLM smells: "
               "{humanizing_rules}, and then write on the topic(s) provided in "
               "these points. Do not add features which aren't present: {points}"

Examples: Two things get in the way of clear Founder identity and narrative:

1. The Fog of War: The first challenge is internal. Your story is still evolving, and you're too deep in the daily chaos to see its shape. You know something profound is happening in your company, but articulating it feels like trying to describe water while swimming. Besides, when the codebase has collapsed in a heap of on-call issues, identity and narrative are the last thing on your mind. You tell yourself you'll figure it out next week. Or the week after. You promise.

2. The Content-First Trap: The second challenge is external. Too many agencies and social media experts jump straight to content without getting context. They ask "What should we post?" before understanding why you're posting in the first place. They can tell you everything about your market position, but nothing about your authentic voice. You want to talk about your tech stack. They want you to pick a fight with Elon. End result? You sound like every other founder on LinkedIn."

Humanizing_rules = don't use the following: “it’s not X, it’s Y” framings, rule-of-three lists, em-dash overuse, “delve/tapestry/landscape,” tidy summary endings, throat-clearing openers"""

Output:

Two things block your content:

1. The Bottleneck: You're one person. Video, voice, image and text each need a different tool and a different day.

2. The Chaos: Five apps, no flow. You post when you remember.

BrewContent automates the whole flow. AI video, voice, image and text in one place. Stop juggling.



# For Kafka

Points given:
Apache Kafka is an open-source, distributed event streaming platform used to collect, store, process, and re-play real-time data feeds at a massive scale
Unlike traditional message queues (like RabbitMQ) that delete a message the moment a consumer reads it, Kafka persists and keeps messages on disk for a set retention period (such as 7 days by default). This allows multiple different teams or services to read the same data independently, replay past events, or recover from system outages



Simple Output:
Apache Kafka: Why Persistence Changes Everything in Event Streaming
Apache Kafka is an open-source, distributed event streaming platform built to collect, store, process, and re-play real-time data feeds at massive scale. From tracking user clicks on e-commerce sites to processing millions of financial transactions, Kafka has become the backbone of modern data infrastructure.

What truly sets Kafka apart from traditional message queues like RabbitMQ? The answer lies in persistence.

With conventional queues, a message is deleted the moment a consumer reads it. The data is gone—consumed and discarded. Kafka takes a fundamentally different approach: it persists messages on disk for a configurable retention period (seven days by default).

This simple design decision unlocks powerful capabilities:

Multiple consumers, one stream: Different teams and services can independently read the same data. Your analytics pipeline, fraud detection system, and notification service can all consume identical events without interfering with each other.

Replay past events: Need to reprocess data after fixing a bug or deploying a new consumer? Simply rewind and replay.

Recover from outages: If a service goes down, it can catch up on everything it missed once it's back online.

In short, Kafka isn't just moving messages—it's building a durable, rewindable record of everything that happens in your system.


Complex output:
Why Kafka Doesn't Delete Your Data (And Why That Matters)
Most engineering teams hit the same wall with traditional message queues: the message vanishes the second someone reads it, and there's no getting it back.

1. The One-and-Done Problem: Traditional queues like RabbitMQ delete a message the moment a consumer picks it up. Sounds efficient until three different teams need the same event. Now you're duplicating topics and hacking fan-out logic to paper over it. When a service crashes mid-processing, that data is just gone. You tell yourself you'll rebuild it from logs. Or the database. You promise.

2. The Disk Is the Feature: Apache Kafka takes a different path. It's an open-source, distributed event streaming platform built to collect, store, process, and re-play real-time data feeds at massive scale. Messages stay on disk for a retention period (7 days by default), so multiple teams and services can read the same data independently, each on their own schedule. A new service joined the party last month? Replay the past events from the beginning. An outage knocked out one of your consumers? It recovers from where things left off once it's back.

RabbitMQ hands you the package and walks away. Kafka keeps a copy on the shelf for a week, just in case.

