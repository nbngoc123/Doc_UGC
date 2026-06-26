# Other Nodes

## **1. Node Graph Starts**

![](./Genshin Impact Miliastra Wonderland_ General Guide10_files/74689be7-f50a-469f-806b-e2bfc8e1fe2f.png)

**Node Functions**

Start event of the Skill Node Graph

Used to customize the Skill logic after this Node; subsequent Nodes execute in the order defined by the Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

##

Flow Control Node

1

Explain

---

# Other Nodes

## **1. Execute Only by Sequence**

![](./Genshin Impact Miliastra Wonderland_ General Guide15_files/c369df44-452e-4101-aaf7-7bd579ec71f3.png)

**Node Functions**

Start Event of the Creation Status Node Graph

The Creation Status Node Graph starts with an [**Execute Only by Sequence]** node. Each output pin connects to an Execution Node, allowing different actions to run as needed. If the entry conditions for the previous action are not met, the graph will enter the *Failed Execution* first. If the conditions are still not met, it will try the action on the next pin

The Creation Status Node Graph runs continuously. If a higher-priority behavior meets its conditions, the Complex Creation immediately switches to execute that behavior

If the conditions are not met, the Complex Creation may not execute any actions

Example: At runtime, Branch 1 checks Node A first. If Node A meets its conditions and executes successfully, Nodes B and C will not execute. If Node A does not meet its conditions, Branch 1 continues by checking Node B. If neither Node A nor Node B meets its conditions, Branch 2 then checks whether Node C meets its conditions

If the Creation is executing the behavior in Node C, but Node A's execution condition is met, the Complex Creation will immediately switch to executing the behavior in Node A

![](./Genshin Impact Miliastra Wonderland_ General Guide15_files/ef35a55a-44fe-48cf-862c-96e1af72ed77.png)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

##

Flow Control Node

1

Explain

---

# Other Nodes

## **1. Execute Only by Sequence**

![](./Genshin Impact Miliastra Wonderland_ General Guide20_files/f27de125-685a-4a28-8e70-83baf42b3f10.png)

**Node Functions**

Start Event for the Creation Status Decision Node Graph

The Creation Status Decision Node Graph starts with an [**Execute Only by Sequence)]** node. Each output pin connects to a **[Switch to self execution status]** node, so you can execute different behaviors as needed. If the entry conditions for the previous state are not met, it will enter the *Failed Execution* first. If the conditions are still not met, it will try the state on the next pin

The Creation Status Decision Node Graph runs continuously. When a state earlier in the sequence meets its conditions, the Complex Creation immediately switches execution state and executes the Status Node Graphs in that preceding order

If no conditions are met, the Complex Creation may not execute any Status Node Graph

Example: At runtime, Branch 1 checks Node A first. If Node A meets its conditions and executes successfully, Nodes B and C will not execute. If Node A does not meet its conditions, Branch 1 continues by checking Node B. If neither Node A nor Node B meets its conditions, Branch 2 then checks whether Node C meets its conditions

If the Creation Status Node Graph in Node C is currently running, but Node A's execution conditions are met, the Complex Creation will immediately switch to the Creation Status Node Graph in Node A

![](./Genshin Impact Miliastra Wonderland_ General Guide20_files/fac529b4-d4a0-40da-9169-97ae8cbe87a4.png)

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

##

Flow Control Node

1

Explain

---

# Other Nodes

## **1. Node Graph Begins**

![](./Genshin Impact Miliastra Wonderland_ General Guide5_files/66ac757a-5bb0-4b47-95c4-e5661de45c0d.png)

**Node Functions**

Start event of the Skill Node Graph

Used to customize the Skill logic after this Node; subsequent Nodes execute in the order defined by the Node Graph

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
|  |  |  |  |

## **2. Node Graph End (Boolean)**

![](./Genshin Impact Miliastra Wonderland_ General Guide5_files/5fe603d7-905b-4d09-a835-6697061225a0.png)

**Node Function**  
End Node for Boolean Local Filter

Outputs True or False as the final result; applies to the referenced logic

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Output Result (Boolean) | Boolean |  |

## **3. Node Graph End (Integer)**

![](./Genshin Impact Miliastra Wonderland_ General Guide5_files/59594bab-9043-4d58-981a-ce6878d80952.png)

**Node Function**  
End Node for Integer Local Filter

Outputs an Integer value as the final result; applies to the referenced logic

**Node Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter Type** | **Parameter Name** | **Type** | **Description** |
| Input Parameter | Output Result (integer) | Integer |  |

##

Flow Control Nodes

1

Explain
