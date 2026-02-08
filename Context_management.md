# Context management
[How to avoid Context Rot](https://research.trychroma.com/context-rot)

Model maintain performance even when context is compressed or filtered, as long as the relevant information is preserved. Models can often "reason through" irrelevant context better than they can filter it for pure information retrieval

For retrieval tasks:
    1. keep only information semantically related to the query.
    2. Place critical facts at start or end (avoid middle)
    3. Remove semantically unrelated content

For reasoning tasks.
    4. Group related information together
    5. Keep reasoning chain elements proximate
    6. More forgiving of middle placement than retrieval



