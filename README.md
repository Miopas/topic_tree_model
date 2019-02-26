# topic_tree_model
A model for dialogue management.

**Still Doing...**

Test case 1:
```console
(parser_env) ✔ ~/miopas/topic_tree_model
18:00 $ python run.py
system output > Hello
Enter your input > {"domain":"flight", "intent":"book", "slots":{"customer_name":"Jack"}}
system output > Please input your departure.
Enter your input >  {"domain":"flight", "intent":"book", "slots":{"start_city":"city_A"}}
system output > Please input your arrival.
Enter your input > {"domain":"flight", "intent":"book", "slots":{"arrive_city":"city_B"}}
system output > END
```

Test case 2:
```
(parser_env) ✔ ~/miopas/topic_tree_model
18:00 $ python run.py
system output > Hello
Enter your input > {"domain":"flight", "intent":"book", "slots":{"customer_name":"Jack"}}
system output > Please input your departure.
Enter your input > {"domain":"flight", "intent":"book", "slots":{"start_city":"city_A", "arrive_city":"city_B"}}
system output > END
```

## Reference
[基于主题森林结构的对话管理模型](http://cslt.riit.tsinghua.edu.cn/~fzheng/PAPERS/2003/0303C_ActaAutomatica-TopicForest_WXJ(ZF).pdf)
