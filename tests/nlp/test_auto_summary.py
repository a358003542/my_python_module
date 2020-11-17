#!/usr/bin/env python
# -*-coding:utf-8-*-


from my_python_module.nlp.auto_summary import auto_summary


def test_auto_summary():
    sample = """
## 编者前言

本文是笔者关于叔本华的人生的智慧一书的整理，编辑和点评。具体中文翻译版本是韦启昌翻译的。按照惯例【】里面的文字为编者所写的文字，脚注里面有很多也是编者所作的工作，然后某些地方编者会自由发挥加上文字着重或者删除符号等等，编者如果精力充沛的话发现某些地方翻译不如人意那么也会试着去找寻原版英文来重新翻译，如此等等不一而足。 

原则上编者不会删减原文，最多是多篇文章组成的文集里面取其精华，但同一篇文章是不会进行原文删减的。不过对于某些无关竟要的脚注和译者脚注，或者其他无关紧要的附录部分等会做出一些取舍。

原书第五章建议与格言部分有点显得是原出版社凑篇幅而故意加进去的，这里将其舍弃了。

## 引言 

在这本书里，所谓的”人生的智慧”这个术语仅仅只是一般意义上的讨论，其是一门艺术，一门讨论如何尽量幸福、愉快地度过一生的艺术。【形而上者谓之道，形而下者谓之器——周易。原翻译引入什么形而下这样的翻译只是徒增晦涩罢了，这里借鉴英文版的 `the common meaning of the term` 稍作翻译调整。】关于这方面的教诲在哲学上可称为“幸福论”。因此，这本著作教导人们如何才能享有幸福的生存。要对“幸福的生存”作出定义的话，那从纯客观的角度考虑，或者更确切地说，通过冷静、缜密的思考（因为这里涉及到主观的判断），这一幸福的生存绝对优于非生存。从这一定义我们就可以这样推论：我们依恋这一生存，就是因为这一生存本身的缘故，而不是出于对死亡的恐惧；并且我们渴望看到这一生存能够永恒地延续。至于人生是否或者能否与如此定义的生存相吻合，这本身就是一个问题。对于这一问题，我的哲学已经清楚无误地给予了否定的答案；但哲学上的幸福论对这一问题却预设了肯定的答案。幸福论的这种肯定答案是基于人的一个与生俱来的错误，这个错误在我的主要著作[^1]的第二卷第四十九章已遭到批判。但要完成诸如幸福论一类的著作，我就只能放弃更高的、属于形而上和道德的审视角度——而我真正的哲学本来就是要引领人们进入这样的审视角度。因此，我在这本书里所作的议论只要是从平常、实用的角度出发，并且保留着与此角度相关的谬误时，那么，这些议论就确实经过了折衷的处理。因此原因，它们的价值就只能是有条件的。其实，Eudamonologie[^2]这个词本身就是一个委婉词。另外，这些议论还说不上完整彻底——其中的一个原因是我所讨论的主题难以穷尽；另一个原因就是如果我要全面讨论这个主题，那么，我就只能重复别人已经说过的话。 

就我的记忆所及，卡丹奴斯那本颇值一读的《论逆境》其目的与我这本箴言书大同小异。它可以作为我这本书的补充。虽然亚里士多德在他的《修辞学》第一部第五章里，掺进了简短的幸福论方面的论述，但那些只是老生常谈。我并没有并没有这些前辈的著作，因为汇集别人的话语并不是我的工作；况且，如果我这样做了，那我书中的观点就不能一以贯之，而观点的连贯性却是这类著作的灵魂。当然，一般来说，各个时代的智者们，都说过同样的话语，而愚人们——也就是各个时代的数不胜数的大多数人——也做着恰恰相反的同一样事情。因此，伏尔泰说过，“**当我们离开这个世界的时候，这个世界还是照样愚蠢和邪恶，跟我们刚来到这个世界的时候所发现的并没有两样。**” 

 



## 基本的划分

亚里士多德把人生能够得到的好处分为三类——外在之物、人的灵魂和人的身体。现在我只保留他的三分法。我认为决定凡人命运的根本差别在于三项内容，他们是： 

1）人的自身：即在最广泛意义上属于人的个性的东西。因此，它包括人的健康、力量、外貌、气质、道德品格、精神智力及其潜在发展。 

2）人所拥有的身外之物：亦即财产和其他占有物。 

3）人向其他人所显示的样子：这可以理解为人在其他人眼中所呈现的样子，亦即人们对他的看法。他人的看法又可分为名誉、地位和名声。 

人与人之间在第一项的差别是大自然确定下来的，由此可推断：这些差别比起第二、三项的差别对于造成人们的幸福抑或不幸福会产生更加根本和彻底的影响——因为后两项内容的差别只是出自人为的划分。人自身拥有的优势，诸如伟大的头脑思想或者伟大的心，与人的地位、出身（甚至王公、贵族的出身）、优厚财富等诸优势相比，就犹如真正的国王比之于戏剧舞台上假扮的国王一样。伊壁鸠鲁的第一个门徒门采多罗斯就曾在他的著作里为他的一个篇章冠以这样的题目：“**我们幸福的原因存在于我们的自身内在，而不是自身之外。**” 确实，对于一个人的幸福，甚至对于他的整个生存的方式，最主要的明显就是这个人自身的内在素质，它直接决定了这个人是否能够得到内心的幸福，因为人的内心快乐抑或内心痛苦首先就是人的感情、意欲和思想的产物。而人自身之外的所有事物，对于人的幸福都只间接发挥影响。因此，同一样外在事物和同一样的境遇对于我们每一个人的影响都不尽相同；就算处在同一样的环境，每一个人都生活在不同的世界中。因为与一个人直接相关的是这一个人对事物的看法、他的感情以及他的意欲活动。外在事物只有在刺激起他的上述东西时才能发挥作
用。每个人至於生活于何样的世界首先取决于这个人对这个世界的理解。这个世界因为各人头脑和精神的差异而相应不同。因此，每个人的世界是贫瘠的、浅薄的和肤浅的，抑或丰富多彩、趣味盎然和充满意义——这视各人的头脑而定。例如，不少人羡慕他人在生活中发现和遇到饶有趣味的事情，其实前者应该羡慕后者所具有理解事物的禀赋才对。在后一种人的技术中，他们所经历过的事情都意味深长，而这一点正可归功于他们的思想禀赋。因为在一个思想丰富的人看来是饶有趣味的事情，对于一个肤浅、庸俗头脑的人来说，同样的事情就只不过是平凡世界里面的乏味一幕而已。这种情形尤其明显见之于歌德和拜伦创作的、明显取材于真实事件的许多诗篇。呆笨的读者会羡慕诗人能有那些其乐无穷的经历，而不是羡慕诗人所具有的伟大的想象力——这种想象力足以化平凡无奇为伟大和优美。同样，一个具忧郁气质的人所看到的悲剧一幕，在一个乐天派的眼里只是一场有趣的冲突，而一个麻木不仁的人则把这视为一件无足轻重的事情。所有这一切都基于这样一个事实：现实生活，亦即当下经历的每时每刻，都由两个部分组成：主体和客体——虽然主体和客体彼此密切关联、缺一不可，就像共同构成水的氧和氢。面对完全一样的客体时，不同的主体就意味着所构成的现实完全不同，反之亦然。由此可知，最美、
最好的客体和呆滞、低劣的主体互相结合只能产生出低劣的现实，情形就像恶劣天气之下观赏美丽风景，又或者以糟糕模糊的照相机拍摄这些风景。或者，我们用更浅显的语言来说吧：正如每个人都囿于自己的皮囊，每个人也同样囿于自己的意识。**一个人只能直接活在自己的意识之中。**因此，外在世界对他帮助不大。在舞台上，演员扮演各种各样的角色：仆人、士兵，或者王侯、将相。但是，这些角色之间的区别只是外在的、皮毛的，这些表面现象之下的内核是一样的；他们都不外乎是可怜、痛苦和烦恼的戏子。在现实生活当中情形也是一样。各人拥有的不同地位和财富赋予了个人不同的角色，但各人的内在幸福并不会因外在角色的不同而产生对应的区别。相反，这些人同样是充满痛苦和烦恼的可怜虫。忧虑和烦恼的具体内容因人而异；但它们的形式，亦即其本质，却大同小异；痛苦和忧虑的程度会存在差别，但这些差别却与人们的地位、财富的差别并不相匹配，亦即和每个人所扮演的角色不相吻合。对于人来说，存在和发生的一切事情总只是直接存在和发生在他的意识里面，所以，很明显，人的意识的构成是首要关键。在大多数情况下，主体意识比呈现在意识中的物象、形态更为重要。一切美妙有趣的事物，经由一个愚人呆滞意识的反映，都会变得枯燥乏味。相比之下，<u>塞万提斯却在一个简陋牢房里写作了他的《堂吉诃德》</u>。构成现实的客体部分掌握在命运的手里，因此是可以改变的；但主体部分是我们的自身，所以，就其本质而言它是不可改变的。因此，尽管在人的一生中，外在变化不断发生，但人的性格却始终如一，这好比虽然有一连串的变奏，但主旋律却维持不变。无人能够脱离自身个性。正如那些动物，不管人们把它们放置在何种环境里，它们仍然无法摆脱大自然为它们定下的不可更改的狭窄局限。这一点解释了诸如：为什么我们在努力使自己宠爱的动物快活的时候，应该把这种努力控制在一个狭窄的范围之内，这是由这动物的本性和意识的局限所决定的。人亦如是。一个人所能得到的属于他的快乐，从一开始就已经由这个人的个性规定了。一个人精神能力的范围尤其决定性地限定了他领略高级快乐的能力。如果这个人的精神能力相当有限，那么，所有来自外在的努力——别人或者运气所能为他做的一切——都不会使他超越只能领略平庸无奇、夹杂着动物性的快乐的范围。他只能享受感观的乐趣、低级的社交、庸俗的消费和闲适的家庭生活。甚至教育——如果教育真的有某些用处的话——就大体而言，也无法在拓宽我们精神眼界方面给人带来大的帮助。因为最高级、最丰富多彩以及维持最为恒久的乐趣是精神思想上的乐趣，尽管我们在年轻的时候，对这一点缺乏充足的认识；但是，能否领略这
些精神思想的乐趣却首先取决于一个人与生俱来的精神思想能力。从这里可以清楚地看到我们的幸福在多大的程度上取决于我们自身，即取决于我们的个性。但在大多数情况下，我们却只是考虑运气、考虑拥有的财产，或者考虑我们在他人心目中的样子。其实，运气会有变好的时候，甚至如果我们内在丰富的话，我们就不会对运气有太多的要求。相比之下，一个头脑呆滞的人终其一生都是头脑呆滞，一个笨蛋至死仍是一个笨蛋，哪怕他身处天堂，被天堂美女所簇拥着。因此歌德说： 



> 大众，不分贵贱， 
>
> 都总是承认： 
>
> 众生能够得到的最大幸运， 
>
> 只有自身的个性。 

 

对于人的幸福快乐而言，主体远远比客体来得重要，任何一切都可以证实这一点。例子包括：饥饿才是最好的调味品，衰老之人对青春美色再难一见钟情，天才和圣人所过的生活等。人的健康尤其远远地压倒了一切外在的好处。甚至一个健康的乞丐也的确比一个染病的君王幸运。一副健康、良好的体魄和由此带来的宁静和愉快的脾性，以及活跃、清晰、深刻、能够正确无误地把握事物的理解力，还有温和、节制有度的意欲及由此产生的清白良心——所有这些好处都是财富、地位所不能代替的。一个人的自身，亦即当这个人单独一人的时候陪
伴自己的、别人对此不能予夺的内在素质，其重要性明显胜于任何他能够占有的财物和他在他人眼中呈现的样子。一个精神丰富的人在独处的时候，沉浸于自己的精神世界，自得其乐；但对于一个冥顽不灵的人，接连不断地聚会、看戏、出游消遣都无法驱走那折磨人的无聊。一个善良、温和、节制的人在困境中不失其乐；但贪婪、妒忌、卑劣的人尽管坐拥万千财富都难以心满意足。如果一个人能够享有自己卓越的、与众不同的精神个性所带来的乐趣，那么，普通大众所追求的大部分乐趣对于他来说，都是纯属多余的，甚至是一种烦恼和累赘。 

因此，贺拉斯在谈论自己时说： 



> 象牙、大理石、图画、银盆、雕像、紫衣， 
>
> 很多人视它们为必不可少， 
>
> 但是有的人却不为这些东西烦心。 

 

<u>苏格拉底在看到摆卖的奢侈物品时，说道：“我不需要的东西可真不少啊！”</u> 

对我们的生活幸福而言，我们的自身个性才是最重要和最关键的，因为我们的个性持久不变，它在任何情况下都在发挥着作用；另外，它有别于我列出的第二、第三项好处，保存这些好处只能听天由命，但自身个性却不会被剥夺。与后两项只是相对的好处相比较，我们自身的价值，可以说是绝对的。由此可知，通过外在的手段去影响和对付一个人要比人们普遍所认为的困难得多。只有威力无比的时间才可以行使它的权利：人在肉体和精神方面的优势逐渐被时间消磨净尽，也只有人的道德气质不受时间的影响。在这一方面，财产和别人的看法当然显得更有优势了。因为时间并不会直接夺走这些好处。它后两项好处的另一个优势就是：因为它们都处于客体的位置，它们的本质决定了任何人都可以得到它们，起码，人们都有占有这些好处的可能。相比之下，对于属于主体的东西我们确实无能为力——它们是作为“神的权利”赋予了人们，并终生牢固不变。所以歌德说： 

 

> 在你降临世上的那一天； 
>
> 太阳接受了行星的问候， 
>
> 你随即永恒地遵循着， 
>
> 让你出世的法则茁壮成长， 
>
> 你就是你，你无法逃脱你自己， 
>
> 师贝尔和先知已经这样说过； 
>
> 时间，力量都不能打碎， 
>
> 那既成的、已成活的形体。 

 

我们唯一能够做到的就是尽可能充分地利用我们既定的个性。因此，我们应该循着符合我们个性的方向，努力争取适合个性的发展，除此之外则一概避免。所以，我们必须选择与我们个性相配的地位、职业和生活方式。 

一个天生筋骨强壮，长得像大力神似的人，如果为外在情势所迫，需要从事某种坐着的职业，去做一些精细、烦琐的手艺活，或者从事学习研究和其他脑力工作——这些工作需要他运用先天不足的能力，而他那出色的身体力量却无从发挥——要是出现这种情况，那这个人终其一生都会感到郁郁不得志。但如果一个人虽然具有异常突出的智力，但其智力却无从得到锻炼和发挥，从事的是一种根本发挥不了他的智力的平庸工作；或者，这工作干脆就是他力不能及的力气活，那么，这个人遭遇的不幸比起第一个人则有过之而无不及。所以我们必须
避免过高估计自己的能力，尤其在我们年少气盛的时候，这可是我们生活中的暗礁。 

人的自身比起财产和他人对自己的看法具有压倒性的优势；由此可知，注重保持身体健康和发挥个人自身才能比全力投入获得财富更为明智。但我们不应该把这一说法错误地理解为：我们应该忽略获得我们的生活必需品。不过真正称为财富的，亦即过分的丰裕盈余，对我们的幸福却帮助不大。所以，很多的有钱人感觉并不快乐，因为这些不快乐的有钱人缺乏真正的精神思想的熏陶，没有见识，也因此缺乏对事物的客观兴趣——而只有这些才可以使他们具备能力从事精神思想的活动。财富除了能满足人的真正、自然的需求以外，对于我们的真正幸福没有多大影响。相反，为了保管好偌大的财产，我们会有许多不可避免的操劳，它们打扰了我们舒适悠闲的生活。对于人的幸福，人的自身确实较之于人所拥有的财富更为重要，但是，常人追求财富比追求精神情趣要来劲千百倍。因此我们看到很多人像蚂蚁似地不眠不休、辛勤劳作，从早到晚盘算着如何增加他们已有的财富。一旦脱离了那狭窄的挣钱领域，他们就一无所知。他们的精神空白一片，因此对挣钱以外的一切事物毫无感知。人生最高的乐趣——精神方面的乐趣——对他们来说，是遥不可及的事情。既然如此，他们就只能忙
里偷闲地寻求那些短暂的、感官的乐趣——它们费时很少，却耗钱很多。他们徒劳地以这类娱乐来取代精神上的享受。在他们生命终结的时候，如果运气好的话，他们真的会挣到一大堆的金钱，这是他们一生的成果；他们就会把这钱留给自己的继承人去继续积累或者任意挥霍。这种人尽管终其一生都板着一副严肃、煞有介事的面孔，但他们的生活仍然是愚不可及的，与其他许多傻乎乎的人生没有多少两样。 

所以，人的内在拥有对于人的幸福才是最关键的。正因为在大多数情形下人的自身内在相当贫乏，所以，那些再也用不着与生活的匮乏作斗争的人，他们之中的大多数从根本上还是感觉到闷闷不乐。情形就跟那些还在生活的困苦中搏斗的人一般无异。他们内在空虚、感觉意识呆滞、思想贫乏，这些就驱使他们投入到社交人群中。组成那些社交圈子的人也正是他们这一类的人，“因为相同羽毛的鸟聚在一块”(荷马语)。他们聚在一块追逐消遣、娱乐。他们以放纵感官的欢娱、极尽声色的享受开始，以荒唐、无度而告终。众多刚刚踏人生活的纨绔子弟穷奢极欲，在令人难以置信的极短时间内就把大部分家财挥霍殆尽。这种作派，其根源确实不是别的，正是无聊——它源自上述的精神贫乏和空虚。一个外在富有、但内在贫乏的富家子弟来到这个世界，会徒劳地试图用外在的财富去补偿内在的不足；他渴望从外部得到一切，这情形就好比试图以少女的汗水去强健自己体魄的老朽之人。人自身内在的贫乏由此导致了外在财富的贫乏。 

至于另外两项人生好处的重要性，不需要我特别强调。财产的价值在当今是人所公认的，用不着为其宣传介绍。比起第二项的好处，第三项的好处具有一种相当缥渺的成分，因为名誉、名望、地位等全由他人的意见构成。每人都可以争取得到名誉，亦即清白的名声；但社会地位，则只有那些国家政府的人才能染指；至于显赫的名望就只有极少数人才会得到。在所有这些当中，名誉是弥足珍贵的；显赫的名望则是人所希望得到的价值至昂的东西，那是天之骄子才能得到的金羊毛。另一方面，只有傻瓜才会把社会地位放置在财产之前。另外，人拥有的财产、物品和名誉、声望是处于—种所谓的互为影响、促进的关系。彼德尼斯说过：“一个人所拥有的财产决定了这个人在他人眼中的价值。”如果这句话是正确的话，那么，反过来，他人对自己的良好评价，能以各种形式帮助自己获取财产。 

  

## 人的自身 

 一个人的自身比起这个人所拥有的财产或者他所给予别人的表象都更能带给他幸福——这一点我们已经大致上认识到了。一个人本身到底是什么，也就是说，他自身所具备的东西，才是最关键的，因为一个人的自身个性永远伴随着他，他所体验的一切都沾上他的个性的色彩。无论他经历何种事情，他首要感受到的是他自己。这一点适用于人们从物质事物中获取的乐趣，而享受精神上的乐趣则更是如此。因此，英语的短语to enjoy one’s self（享受）是一个相当生动的表述。例如：人们说：“He enjoys himself in Paris”（他在巴黎享受自己），而不是说“他享受巴黎”。如果一个人的自身个性相当低劣，那么所有的乐趣都会变味，就像把价值不菲的美酒倒进被胆汁弄得苦涩难受的嘴里一样。因此，除了严重灾祸以外，人们在生活中所遭遇到的事情，不论是好是坏，其重要性远远不及人们对这些事情的感受方式；也就是说，人们对事情的感受能力的本质特性和强弱程度才更为重要。一个人的自身是什么，他的自身拥有到底为何，简而言之：他的个性及其价值才唯一直接与他的幸福有关。除此之外的一切都只是间接发挥作用，这些作用因此是可以消除的。但个性发挥的作用却永远无法消除。

因此，针对他人自身优点而产生的嫉妒是最难消除的；所以这种嫉妒会被很小心、谨慎地掩藏起来。进一步而言，只有感觉意识的构成才是恒久保持的，人的个性每时每刻都持续地发挥着作用；相比较而言，除此以外的任何其他东西都永远只是暂时地、偶尔地产生作用，并且它们都受制于不断发生的各种变化。所以，亚里士多德说过：“我们能够依靠的只是我们的本性，而不是金钱。”正因为这样，我们能够咬紧牙关承受纯粹从外而至的灾祸，但由我们的自身所招致的不幸却更难忍受；因为运气会有变好的时候，但我们的自身构成却永远不会
改变。因此，对于人的幸福起着首要关键作用的，是属于人的主体的美好素质，这些包括高贵的品格、良好的智力、愉快的性情和健康良好的体魄——一句话，“健康的身体加上健康的心灵”（尤维纳利斯语）。所以我们应该多加注意保持和改善这一类的好处，而不是一门心思只想着占有那些身外的财产、荣誉。 

在上述这些主体的美好素质当中，最直接带给我们幸福的莫过于轻松、愉快的感官。因为这一美好的素质所带来的好处是即时呈现的，一个愉快的人总有他高兴愉快的原因，原因就是：他就是一个愉快的人。一个人的这种愉快气质能够取代一切别的内在素质，但任何别的其他好处都不可以替代它。一个人或许年轻、英俊、富有和备受人们的尊重，但如果要判断这个人是否幸福，那我们就必须问一问自己：这个人是否轻松愉快？如果他心情愉快，那么，他是年轻抑或年老，腰板挺直抑或腰弯背驼，家财万贯抑或一贫如洗——这些对他而言，都是无关重要的：反正他就是幸福的。我在年轻的时候，有一次翻开了一本旧书，赫然入目的是这样一句话：“谁经常笑，谁就是幸福的；谁经常哭，谁就是痛苦不幸的。”这是一句再普通不过的话了，但我却一直无法把它忘记，因为这句话包含着朴素的真理，虽然这老生常谈说得夸张了点。<u>因此，当愉快心情到来之时，我们应该敞开大门欢迎它的到来，因为它的到来永远不会不合时宜。</u>但我们往往不是这样做：我们经常会犹豫不决地接受愉快的心情——我们想先弄清楚我们的高兴和满足是否确有根据。又或者，我们担心在严肃地盘算和认真地操劳之际，高兴的心情会打扰了我们。其实，这种做法是否真有好处仍是一个未知数。<u>相比之下，高兴的心情直接就使我们获益。它才是幸福的现金，而其他别的都只是兑现幸福的支票。</u>高兴的心情在人们感受高兴的此时此刻就直接给人以愉快。所以，对于我们的生存，它是一种无与伦比的恩物，因为我们生存的真实性就体现在此时此刻——它无法割裂地连接无尽的过去和将来。由此可见，我们应把获得和促进愉快的心情放在各种追求的首位。确实，能够增进愉快心情的莫过于健康；但对于愉快心情贡献最小的则是充裕盈余的金钱财富。那些低下的劳作阶层，特别是在乡下生活的人们，常常露出高兴和满足的表情，而富贵人家却通常感到烦恼。因此，我们应该着重获得和保持身体健康——愉快的心情就是从健康的身体里长出的花朵。众所周知，保持身体健康的手段无非就是避免一切纵欲放荡的行为、令人不快和剧烈的情绪动荡，以及长时间、紧张的精神劳累；每天至少在户外进行两个小时的身体快速运动；勤洗冷水浴，饮食有节。如果一个人每天不进行一定的身体活动，那他就无法保持健康。一切生命活动程序，如果要保持运作正常的话，那么，生命活动程序所在的整体也好，作为这一整体里面的一部分也好，都需要得到运动。因此，亚里士多德说得很对，“**生命在于运动，生命的本质在于运动。**” 身体组织的内部在永不停歇地快速运动；心脏在复杂的双重收缩和舒张的过程中，强劲地、不知疲倦地跳动；心脏每跳动28次，就把身体的全部血液沿着身体的大、小血脉传送一遍，肺部一刻不停地抽气，就像一台蒸汽机；大肠则像虫子一样地蠕动不已；体腺始终在吸收和排泄；伴随着一次脉搏跳动和每一次呼吸，大脑本身就完成了一次双重运动。这样，如果人不进行外在的运动——很多人的生活方式都是静止缺少运动的——那他们身体外表的静止就会与内在进行着的运动形成惊人的、有害的不协调。身体内部不停的运动需要得到某种外在运动的配合与支持。上述身体内外之间的不协调就类似于：某种情绪使我们的内在沸腾激动起来，但却不得不竭力压制这种情绪从我们外表流露出来。甚至树木的生长茂盛也必须借助风的吹动。“每一运动的速度越快，那这一运动就越成其为运动”——这一句话以最简洁的拉丁文表示，就是“Omnis motus guo celerior，eo magis motus”——这一规则可以适用在这里。我们的幸福取决于我们的愉快情绪，而愉快情绪又取决于我们身体的健康状况。关于这点，只要互相对照一下我们在健康、强壮的日子里和当疾病降临、我们被弄得苦恼焦虑的时候，外在境况和事件所留给我们的不同的感觉印象，一切就都清楚了。使我们快乐或者忧伤的事物，不是那些客观、真实的事物，而是我们对这些事物的理解和把握。这就是爱比克泰德所说的“扰乱人们的不是客观事情，而是人们对客观事情的见解”。


我们的幸福十占其九依赖于我们的健康。只要我们保持健康，一切也就成了快乐的源泉；但缺少了健康，一切外在的好处——无论这些好处是什么——都不再具有意义，甚至那些属于人的主体的好处，诸如精神思想、情绪、气质方面的优点等，仍会由于疾病的缘故而被大打折扣。由此看来，人们在彼此相见时首要询问对方的健康状况，并祝愿对方身体健康的做法也就不是没有根据的了，因为健康对于一个人的幸福的确是头等重要的事情。我们可以由此得出这样的结论：最大的愚蠢也就是为了诸如金钱、晋职、学问、声名，甚至为了肉欲和其他片刻的欢娱而献出自己的健康。我们更应该把健康放在第一位。 

虽然健康能极大地增进我们的愉快心情——这种愉快心情对于我们的幸福头等重要——但愉快的心情却不完全依赖于健康；因为即使是完全健康的人也会生成忧郁的气质和沮丧的心情。在这里，最根本的原因无疑在于人的最原初的、因而也是不可改变的机体组织的构成；也就是说，大致上在于一个人的感觉能力与肌肉活动、兴奋能力及机体新陈代谢能力之间构成的正常程度不一的比例。超常的感觉能力会引致情绪失衡、周期性的超乎寻常的愉快或者挥之不去的忧郁。天才的条件就是具备超越常人的神经力量——亦即超常的感觉能力。所以，亚里士多德相当正确地认为：所有杰出、优越的人都是忧郁的：“所有那些无论是哲学、政治学、诗歌或其他艺术方面表现出色的人，看上去都是忧郁的”。西塞罗在讲述下面这句经常被人们引用的话时，他所指的肯定也是上述那段话：“亚里士多德说，所有的天才人物都是忧郁的。”我在这里对人的与生俱来的基本情绪——它因人而异——所作的考察，莎士比亚曾经异常优美地加以描述： 

 

> 大自然造就了奇特的人，
>
> 一些人总是眯缝着眼睛，大声笑着， 
>
> 就像看见苏格兰风笛手的鹦鹉； 
>
> 也有一些人阴沉着面孔，笑不露齿， 
>
> 虽然奈斯特发誓那笑话的确值得一笑。 
>
> ——《威尼斯商人》 

 

柏拉图用了“郁闷”和“愉快”这样的词语来形容这两种不同情绪，出现这些不同情绪是因为不同的人有着极为不同的感受愉快和不愉快印象的能力。因此，一件使一个人近乎绝望的事情，会让另一个人高兴发笑。一般而言，一个人接受愉快印象的能力越弱，那他接受不愉快印象的能力也就越强，反之亦然。同一件事情有出现好或不好两种结果的可能。“郁闷”型的人会因为“不好”的结果而感到悲哀和烦躁，对好的结果也提不起高兴劲儿。“愉快”型的人却不会为不幸的结果悲哀和烦恼，但对事物的好结果却会深感高兴。对“郁闷”型的人来说，尽管他们实现了十个目标中的九个，他们仍然不会为已实现了的目标高兴，而仅仅因为一个目标的落空而烦恼、生气。愉快型的人则相反，他们会从成功实现了的目标那里取得安慰和愉快。【愉快型的人想到明天还有面包吃就知足了，郁闷型的人明年甚至几十年之后有没有面包吃也是他们忧愁伤心的原因。】不过，正如没有一丁点好处的十足坏事并不容易找到，同样，“郁闷”型的人，亦即阴沉和神经兮兮的人，虽然总的来说比无忧无虑、快乐的人承受更多只是想象出来的不幸和苦难，但却因此而遭遇更少真实的不幸和苦难因为他们把一切都看成漆黑一团，总是把事情往最坏的方面想，并因此准备着防范措施。这样，与那些总是赋予事情以愉快色彩和大好前景的人相比，他们更少失算与栽跟斗。但如果一个天生具有不满、易怒心态的人，再加上神经系统或者消化器官疾病的折磨，情况最终可以发展成这个样子：持续的不幸引致了对生活的厌烦，并由此萌生了自杀的倾向。由于这个原因，最微不足道的不便和烦恼都会引致自杀的结果。的确，当情况变得最糟糕的时候，甚至连这点不便和烦恼也不需要了，一个人会纯粹由于持续闷闷不乐的心情而决定自杀。这种人会以冷静的思考和铁
定的决心实施自杀行为。这种情况经常发生：一个病人尽管处于别人的监视之下，仍会随时留意着利用每个不被监视的机会，迫不及待地抓住这现在对于他来说是求之不得的和最自然不过的解脱痛苦的手段——整个过程没有犹豫、退缩和内心斗争。关于自杀方面的详尽论述，可阅读埃斯基罗尔的《精神疾病》一书。但除此之外，在某种情况下，就算是最健康的和或许是最愉快的人也会想到过自杀。那就是当痛苦非常巨大，或者，步步逼近的不幸实在不可避免，这一巨大的痛苦或不幸已经压倒了对死亡的恐惧。不同之处只在于自杀所必需的诱因的大小，这一诱因和人的不满情绪成反比例。不满情绪越厉害，则自杀所需的诱因就越小，到最后，诱因可以减至为零。相比之下，愉快情绪越强烈，维持这一情绪的健康状况越良好，自杀的诱因就必须越大。因此，导致自杀的原因大小不一，但构成两个极端的就是：与生俱来的忧郁不满的心理得到了病态的加剧；天性是健康、愉快的，只是客观的原因所致。 

健康和美貌有着部分的关联，虽然美貌这一属于主体的好处不会直接带给我们幸福——它只是间接通过留给别人印象的方式做到这点——但美貌仍然是至为重要的，甚至对男人来说也是如此。良好的长相是一纸摊开的推荐书，它从一开始就为我们赢得了他人的心。因此，荷马这些诗句尤其适用于我在这里所说的话： 

 

> 神祇的神圣馈赠不容遭到蔑视， 
>
> 这些馈赠只能经由神祇的赐予。 
>
> 任何人都无法随心所欲地获取它们。 
>
> ——《伊利亚特》 

 

对生活稍作考察就可以知道：痛苦和无聊是人类幸福的两个死敌，关于这一点，我可以作一个补充：每当我们感到快活，在我们远离上述的一个敌人的时候，我们也就接近了另一个敌人，反之亦然。所以说，我们的生活确实就是在这两者当中或强或弱地摇摆。这是因为痛苦与无聊之间的关系是双重的对立关系。一重是外在的，属于客体；另一重则是内在的，属于主体。外在的一重对立关系其实也就是生活的艰辛和匮乏产生出了痛苦，而丰裕和安定就产生无聊。因此，我们看见低下的劳动阶层与匮乏——亦即痛苦——进行着永恒的斗争，而有钱的上流社会却旷日持久地与无聊进行一场堪称绝望的搏斗。而内在的或者说属于主体的痛苦与无聊之间的对立关系则基于以下这一事实：一个人对痛苦的感受能力和对无聊的感受能力成反比，这是由一个人的精神能力的大小所决定的。也就是说，一个人精神的迟钝一般是和感觉的迟钝和缺乏兴奋密切相关的，因此原因，精神迟钝的人也就较少感受到各种强度不一的痛苦和要求。但是，精神迟钝的后果就是内在的空虚。这种空虚烙在了无数人的脸上。并且，人们对于外在世界发生的各种事情——甚至最微不足道的事情——所表现出的一刻不停的、强烈的关注，也暴露出他们的这种内在空虚。人的内在空虚就是无聊的真正根源，它无时无刻不在寻求外在刺激，试图借助某事某物使他们的精神和情绪活动起来。他们做出的选择真可谓饥不择食，要找到这方面的证明只须看一看他们紧抓不放的贫乏、单调的消遣，还有同一样性质的社交谈话，以及许许多多的靠门站着的和从窗口往外张望的人。正是由于内在的空虚，他们才追求五花八门的社交、娱乐和奢侈；而这些东西把许多人引人穷奢极欲，然后以痛苦告终。使我们免于这种痛苦的手段莫过于拥有丰富的内在——即丰富的精神思想。因为人的精神思想财富越优越和显著，那么留给无聊的空间就越小。这些人头脑里面的思想活泼奔涌不息，不断更新；它们玩
味和摸索着内在世界和外部世界的多种现象；还有把这些思想进行各种组合的冲动和能力——所有这些，除了精神松弛下来的个别时候，都使卓越的头脑免受无聊的袭击。但是，突出的智力是以敏锐的感觉为直接前提，以强烈的意欲，亦即强烈的冲动和激情为根基。这些素质结合在一起提高了情感的强烈程度，造成了对精神，甚至肉体痛苦的极度敏感。对任何不如意的事情，甚至细微的骚扰，都会感觉极度不耐烦。所有这些素质大大加强了头脑里面事物的各种表象，包括拂逆人意的东西。这些表象由于头脑强烈的想象力的作用而变得生动活泼。我这里所说的比较适用于所有各种精神思想能力参差不一的人，从最呆笨的头脑一直到最伟大的思想天才。由此可知，无论从客体抑或从主体上说，如果一个人距离人生痛苦的其中一端越近，那他距离痛苦的另一端也就越远。据此，每个人的天性都会指导自己尽可能地调节客体以适应主体，因而更充足地做好准备以避免自己更加敏感的痛苦一端。一个精神富有的人会首先寻求没有痛苦、没有烦恼的状态，追求宁静和闲暇，亦即争取得到一种安静、简朴和尽量不受骚扰的生活。因此，一旦对所谓的人有所了解，他就会选择避世隐居的生活；如果他具备深邃、远大的思想，他甚至会选择独处。因为一个人自身拥有越丰富，他对身外之物的需求也就越少，别人对他来说就越不重要。所以，一个人具备了卓越的精神思想就会造成他不喜与人交往。的确，如果社会交往的数量能够代替质量，那么，生活在一个熙熙攘攘的世界也就颇为值得的了。但遗憾的是，一百个傻瓜聚在一起，也仍然产生不了一个聪明的人。相比之下，处于痛苦的另一极端的人，一旦匮乏和需求对他的控制稍微放松，给他以喘息的机会，他就会不惜代价地寻找消遣和人群，轻易地将就一切麻烦。他这样做的目的不为别的，只是为了逃避他自己。因为在独处的时候，每个人都只能返求于自身，这个人的自身具备就会暴露无遗。因此，一个愚人背负着自己可怜的自身——这一无法摆脱的负担——而叹息呻吟。而有着优越精神思想禀赋的人却以其思想使所处的死气沉沉的环境变得活泼和富有生气。因此，塞尼加所说的话是千真万确的：“愚蠢的人受着厌倦的折磨”。同样，耶稣说：“愚人的生活比死亡还要糟糕。”因此，我们可以发现：大致而言，一个人对与人交往的爱好程度，跟他的智力的平庸及思想的贫乏成正比。人们在这个世界上要么选择独处，要么选择庸俗，除此以外再没有更多别的选择了。 

人的大脑意识是人的身体的寄生物，它寓寄在人的身体之中，而人们辛苦挣来的闲暇，就是为了让人能够自由地享受意识和个性所带来的乐趣。所以，**闲暇是人生的精华**，除此之外，人的整个一生就只是辛苦和劳作而已。但闲暇给大多数人带来了什么呢？如果不是声色享受和胡闹，就是无聊和浑噩。人们消磨闲暇的方式就显示出闲暇对于他们是何等的没有价值。他们的闲暇也就是阿里奥斯托所说的“一无所知者的无聊”。凡夫俗子只关心如何去打发时间，而略具才华的人却考虑如何好好利用时间。头脑思想狭隘的人容易受到无聊的侵袭，其原因就是他们的智力纯粹服务于他们的意欲，是意欲的工具。如果诱发意欲的动因暂时没有出现，那么，意欲就休息了，智力也就放假了——因为智力和意欲不一样，它不会自动活动起来。这样，人身上的所有力量可怕地迂滞静止，这也就是无聊。为了应付无聊，人们就为意欲找出一些琐碎、微小、随意和暂时的动因以图刺激意欲，和以此激活智力——因为智力的任务本来就是理解、把握动因。但这些动因较之于那些真正的、自然的动因，就犹如纸币比之于银元，因为前者的价值是有随意性的；诸如游戏、玩纸牌等就属于这一类的动因。这
些游戏的发明也就是为了上述目的。如果没有了这些游戏，缺乏思想的人就会敲击随便一件伸手可及的物品来帮助自己打发时光。对这种人而言，雪茄同样是一件受欢迎的代替思考的物品。因此，在各国，玩纸牌成了社交、聚会的主要娱乐。它反映了这种社交聚会的价值，也宣告了思想的破产。因为人们彼此之间没有可以交换的思想，所以，他们就交换纸牌，并试图赢取对方的金钱。可怜的人啊！但我不想有欠公正地压制这样的想法，那就是我们可以为玩纸牌游戏作这样的辩护：玩纸牌不失为一种应付以后的世俗生活的演习，只要我们通过玩牌能学习到如何巧妙地运用那听任偶然的、不可更改的既定形势（牌局），使我们尽量得到我们所能得到的东西；为此目的，人们必须养成习惯保持沉着，即使牌势恶劣的时候，仍能装出一副高兴的外表。不过，正因为这样，玩牌也就会产生一种伤风败俗的作用。这种游戏的特质就在于人们动用一切诡计和技巧，不择手段地去赢取他人的财物。这种在游戏里面体验和获得的习惯，会在人的实际生活里生根、蔓延。这样，人们逐渐在处理人与人之间的事务中，也同样依照这种习惯行事，认为只要法律允许，就可以利用掌握在手的每一个优势。这方面的例证在日常生活中俯拾皆是。正如我已经说过的，闲暇就是每一个人的生命存在开出的花朵，或者毋宁说是果实。也只有闲暇使人得以把握、支配自身，而那些自身具备某些价值的人才可以称得上是幸福的。但对于大多数人来说，闲暇只会造就一个无用的家伙，无所事事，无聊烦闷，他的自身变成了他的包袱。因此，我们应该庆幸：“亲爱的兄弟们，我们不是干粗活女工的孩子，我们是自由的人”。 

进一步而言，正如一个不需要或只需要很少进口物品的国家是最幸运的国家。同样，如果一个人内在充足、丰富，不需要从自身之外寻求娱乐，那么，他就是一个最幸运的人。因为进口物品使国家花费不菲，仰仗他人，同时又带来危险、制造麻烦。到头来，这些物品只能是我们本土产品的糟糕的代替品，因为无论如何，<u>我们不应该从他人那里，或者从自身之外期望太多。</u>一个人对另一个人所能做的只是极为有限。归根到底，每个人都孑然独立，这时候，最关键的问题就是这单独的人是个什么样的人。因此，歌德的评论（《诗与真》）适用于这里：无论经历任何事情，每个人都最终都得返求于己。或者，就像奥立弗·高尔斯密的诗句说的： 

 

> 无论身在何处， 
>
> 我们只能在我们自身寻找或者获得幸福 
>
> ——《旅行者》 

 

因此，每个人都要充分发挥自己的所能，努力做到最好。一个人越能够做到这一点，那他在自己的身上就越能够发现快乐的源泉，那他也就越幸福。亚里士多德无比正确地说过：**幸福属于那些能够自得其乐的人。**这是因为幸福和快乐的外在源泉，就其本质而言，都极其不确定，并且为时短暂和受制于偶然。因此，甚至在形势大好的情况下，它们仍然会轻易终结。的确，只要这些外在源泉不在我们的控制之下，那这种情形就是不可避免的。人到老年，几乎所有这些外在源泉都必然地干枯了，因为谈情说爱、戏谑玩笑、对旅行的兴趣、对马匹的喜好，以及应付社交的精力都舍我们而去了；甚至我们的朋友和亲人也被死亡从我们的身边一一带走。此时此刻，一个人的自身拥有，比起以往任何时候都更加重要，因为我们的自身拥有能够保持得至为长久。不过，无论在任何年龄阶段，一个人的自身拥有都是真正的和唯一持久的幸福源泉。我们这个世界乏善可陈，到处充斥着匮乏和痛苦，对于那些侥幸逃过匮乏和痛苦的人们来说，无聊却正在每个角落等待着他们。此外，在这个世界上，卑劣和恶毒普遍占据着统治的地位，而愚蠢的嗓门叫喊得至为响亮，他们的话语也更有分量。命运是残酷的，人类又是可怜可叹的。生活在这样的一个世界里，一个拥有丰富内在的人，就像在冬月的晚上，在漫天冰雪当中拥有一间明亮、
温暖、愉快的圣诞小屋。因此，能够拥有优越、丰富的个性，尤其是深邃的精神思想，无疑就是在这地球上得到的最大幸运，尽管命运的发展结果不一定至为辉煌灿烂。因此，年仅19岁的瑞典克里斯汀女王在评论笛卡尔时——她只是通过笛卡尔的一篇论文以及一些口头资料了解到这位已经在荷兰孤独生活了20年的人——说了一句充满睿智的话：笛卡尔先生是我们所有人当中最幸福的一个；在我看来，他的生活令人羡慕（《笛卡尔的一生》，巴叶著）。当然，就像笛卡尔的情形那样，外部环境必须允许我们支配自身，并从中汲取快乐。所以圣经《传道书》已经说过：“智慧再加上一笔遗产就美好了，智慧帮助一个人享受阳光。”谁要是通过大自然和命运的恩赐，交上好运得到内在的财富，那他就要小心谨慎地确保自己幸福的这内在源泉畅通无阻。但要达到这一目的，条件就是拥有独立和闲暇。因此，这种人会乐意以俭朴和节制换取上述二者。如果他们不像其他人那样依赖快乐的外在源泉，情况就更是如此。因此，对职位、金钱、世人的赞许和垂青等诸如此类的指望终究不会把这种人诱入歧途，牺牲自己以迎合人们卑微的目的或者低下的趣味。有机会的话，他就会像贺拉斯在给默斯那斯的信中所建议的那样做。为了外在的荣耀、地位、头衔和名声而部分或全部地奉献出自己的内在安宁、闲暇和独立——这是极度的愚蠢行为。歌德就是这样做了。但我的守护神却明确地指引我走向与此相反的方向。 

我们在这里讨论的真理，即幸福源自于人的内在，被亚里士多德的真知灼见所引证（《伦理学》）。他说：每一快乐都是以人从事某种活动，或者应用人的某种能力作为前提；没有这一前提，快乐也就无从谈起，亚里士多德的教导——即人的幸福全在于无拘束地施展人的突出才能——与斯托拜阿斯对逍遥派伦理学的描述如出一辙。斯托拜阿斯说：“幸福就是发挥、应用我们的技巧，并取得期待的效果。”他特别说明他所用的古希腊字词指的是每一种需要运用技巧和造诣的活动。大自然赋予人们以力量，其原始目的就是使人能够和包围着人们的匮乏作斗争。一旦这场斗争停止了，那再也派不上用场的力量就会成为人的负担。因此，他必须为它们找到消遣，亦即不带任何目的地运用这些力量。因为如果不这样做，人就会马上陷入人生的另一个痛苦——无聊——之中。因此，王公、巨富尤其受到无聊的折磨。关于他们的痛苦，卢克莱修留给我们这样一段描写。当今我们在每个大城市，每天都有机会见到类似的例子： 

 

> 他经常离开偌大的宫殿，匆匆走向室外露天——因为在屋子里他感到厌烦——直到他突然返回为止，因为他感觉出门并没有好得了多少。又或者，他策马驰往乡村庄园，就好像他的庄园燃起了大火，他必须匆忙赶去扑救一样。但刚跨进乡村庄园的门槛，他就无聊地呵欠连连，或者干脆倒头大睡。他要尽力去忘记自己，直到他想返回城市为止。 

 

这些先生们在年轻的时候，肌肉力量和生殖能力都旺盛十足。但随着岁月的流逝，只有思想能力才能保留下来。如果我们的思想能力本身就有所欠缺，或者，我们的思想能力没有得到应有的锻炼，又或者，我们欠缺能发挥思想能力的素材，那我们将遭遇到的悲惨情形就着实令人同情。意欲是唯一无法枯竭的力量，它受到激情的刺激就会抬头。例如，意欲可以通过一掷千金的豪赌——这一真正低级趣味的罪恶——而被鼓动起来。一般来说，每个无事可做的人都会挑选一种能够运用自己的特长的消遣，比如下棋、玩牌、狩猎、绘画、赛马、玩九柱戏；或者研究文章、音乐、诗歌或者哲学。我们可以探索人的能力的所有外在表现的根源，亦即深入到人的三种生理基本能力，从而对这个课题有一个彻底的了解。我们也就需要考察这三种能力的那些不带目的的发挥和活动——它们的发挥和活动构成了人的三类快乐的源泉。每个人都会有适合自己的一类快乐，这由他身上所突出具备的是哪一种能力而定。第一类是为机体新陈代谢能力所带来的乐趣：这包括吃喝、消化、休息和睡觉。在一些国家，这类快乐获得首肯，这类活动甚至成为全民性的娱乐。第二类是发挥肌肉力量所带来的乐趣：这些包括步行、跳跃、击剑、骑马、舞蹈、狩猎和各种各样的体育游戏；甚至打斗和战争也包括在内。第三类为施展感觉能力方面的乐趣：这些包括观察、思考、感觉、阅读、默想、写作、学习、发明、演奏音乐和思考哲学等。关于这各种各样的乐趣的等级和价值，以及它们所能维持的时间，会有诸多说法，读者们也尽可以作出补充。但我们应该清楚：我们感受的乐趣（它以运用、发挥我们的能力为前提）和幸福（它由乐趣的不断重复所构成）越大，那作为前提的力量也就越高级。并且，没有人会否认，在这一方面，感觉能力比人的另外两种基本生理力量更为优越——人较之于动物在感觉方面的明显优势就是人优胜于动物之处，但人的另外两种基本生理能力在动物身上也同样存在，甚至远胜于人类。感觉能力隶属于人的认知能力；因此，卓越的感觉力使我们有能力享受到属于认知的，亦即所谓精神思想上的乐趣。情感能力越卓越和明显，那么，我们所享受到这方面的乐趣就越大[^3]。要使一个凡夫俗子对某事物产生热切的关注，只能通过刺激他的意欲，并由此提起他对这事物的切身兴趣。但是意欲持久的兴奋，却不是单一纯净、不含杂质的，它是与痛苦紧密相联。在上流社会流行的纸牌游戏就是这样一种旨在刺激意欲的手段。的确，它能激发起人们肤浅的兴趣，但它带给人们的也只是暂时的、轻微的、而不是永久和严重的痛苦。正因为如此，我们只能把纸牌游戏视为对意欲的搔痒式的挑逗[^4]。相比之下，具有优越精神能力的人却能够最热切地全情投入到认知活动中去，这里面不夹杂任何意欲的成分。事实上，他们这样热切投入也是迫不得已的事情。在他们全情投入其中的领域里，痛苦是陌生的。我们可以说，他们置身于神灵轻松自在地生活的地方。所以，大众的生活把大众引向浑噩、呆滞，他们的思想和欲望无一不是指向维护他们的个人安逸的那些渺小事务，正因为这样，他们的生活也就迈向了形形色色的苦难。所以，一旦他们停止为这些目标操劳，并且不得不返回依赖他们的自身内在时，无法忍受的无聊就向他们袭来。这时候，只有情欲的疯狂火焰，才可以活动一下那呆滞和死气沉沉的众生生活。但精神禀赋卓越的人却过着思想丰富、生气勃勃和意味深长的生活；有价值和有兴趣的事物吸引着他们的兴趣，并占据着他们的头脑。这样，最高贵的快乐的源泉就存在于他们的自身。能够刺激他们的外在事物是大自然的杰作和他们所观察的人类事务，还有那各个时代和各个地方的天才人物所创造的为数众多、千姿百态的杰作。只有这种人才可以真正完全地享受到这些杰作，因为只有他们才充分理解和感受到它们。因此，那些历史上的杰出人物才算是真正为他们活着，前者其实在向这些人求助了。而其他的人则只是偶然的看客，他们只是部分地明白个中的东鳞西爪。当然，具有天赋的人比常人多一个需求，那就是，学习、观察、研究、默想和实践的需求。因此，这也就是对闲暇的需求。但是，正如伏尔泰所正确无误地说过的，“只要有真正的需求，才会有真正的快乐。”所以，有这样的需求就是这些人能够得到别人所没有的快乐的条件。而对于其他人来说，尽管他们的周围存在各种各样大自然的美、艺术的美，以及思想方面的杰作，但是这些东西从根本上对于他们就像艳妓之于年老体衰的人。因此，一个具有思想天赋的人过着双重的生活，一种是他个人的生活，另一种则是思想上的生活，后者逐渐成为了他的唯一目标，而前者只是作为实现自己目标的一种手段而已。但对于芸芸众生来说，只有浅薄、空虚和充满烦恼的生存才会被视为是生活的目标。精神卓越的人首要关注的是精神上的生活。随着他们对事物的洞察和认识持续地加深和增长，他们的生活获得了一种整体的统一；精神生活的境界稳步提升而变得完整、美满，就像一件逐步变得完美的艺术品。与这种精神生活相比，那种纯粹以追求个人自身安逸为目标的实际生活则显得可悲——这种生活增加的只是长度而不是深度。正如我已经说过的，这种现实生活对于大众就是目的，但对于精神卓越者而言，那只是手段而已。 

我们的现实生活在没有受到情欲的驱动时会变得无聊和乏味；一旦受到情欲的驱动，很快就会变得痛苦不堪。因此，只有那些思想禀赋超常的人才是幸运的，他们的智力超出了意欲所需要的程度。只有这种人才能够在过着实际生活的同时，还享有一种不带痛苦的精神生活。他们全副身心地沉浸在这种精神生活当中，乐此不疲。仅仅拥有闲暇，即智力不需要为意欲服务，并不足以使人们享有精神生活；为能享有精神生活，人们必须具备某种真正充裕有余的能力。只有具备了这种充裕有余的能力，才能有资格从事并不服务于意欲的纯粹精神上的活动。相比之下，“没有精神思想消遣的闲暇就是死亡，它就像要把人活生生地埋葬”（塞尼加语）。根据各人精神思想能力参差不一的充裕程度，而相应在现实生活的同时，还有着无数等级的思想生活：从仅仅只是收集和描绘昆虫、鸟类、矿物、钱币之类的精神乐趣，一直到创作出最杰出的文学和哲学作品。类似的精神生活使我们得以避免低劣的社交，以及许许多多的危险、不幸、损失和纵欲。如果人们完全是在这个现实生活里追求幸福，那他们就会遭遇上述这些不好的东西。所以，例如，虽然我的哲学并没有给我带来具体的好处，但它却使我避免了许多的损失。 

但是，常人却寄希望于身外之物，寄望于从财产、地位、妻子、儿女、朋友、社会人群那里获取生活快乐；他把自己一生的幸福寄托在这些上面。因此一旦他失去了这些东西，或者对这些东西的幻想破灭，那他的幸福也就随之烟消云散了。为把这种情形表达清楚，我们可以这样说：这个人的重心在他的自身之外。正因为这样，常人的愿望和念头总是不停地转换。如果能力允许他这样做，他就会变换着花样，购买乡村别墅或者良种马匹；一会儿举行晚会，一会儿又出外旅游。总之，他要极尽奢华的享受，这是因为他只能从外在出发寻找得到满
足，这就像重病人一样，冀望通过汤水和药物重获身体的健康和力量。其实，一个人自身的生命力才是身体力量和健康的源泉。我们并不马上讨论处于对应的另一极端的人，我们首先看看那些精神思想力量并不那么显著突出、但却又超越了泛泛之辈的人吧。我们可以看到：当缺少外在的快乐源泉，又或者，当那些外在的快乐渠道再也无法满足他们的时候，这一类人就会学习和练习某一门优美的艺术，或者进行其他的自然科学的学习。例如：研究植物学、矿物学、物理学、天文学、历史学等等，并从中得到消遣和乐趣。对于这样的人，我们才可以说，他们的重心是部分地存在于自身。但是，这些人对艺术的业余爱好与自发的艺术创造力之间仍然存在一段相当的距离；又因为单纯的自然科学知识只停留在事物表面现象之间的相互关系，所以，他们无法全副身心投入其中，被它们所完全占据，并因此整个的生命存在与这些东西紧密地纠缠在一起，以至于对除此之外的任何事物都失去了兴趣。只有那些具有最高等的精神禀赋、我们称之为“天才”的一类人才会进入这样的状态，因为只有这些人才会把存在和事物的本质，完全而又绝对地纳入他们的课题。在这以后，他们就尽力把自己的深刻见解，以适合自己个性的方式，或通过艺术，或通过哲学表达出来。因此，对于这一类人来说，不受外界的打扰，以便忙于自己的思想和作品，实在已经成为迫切的需要。孤身独处正是他们求之不得的，闲暇则是至高无上的赐予。其他别的一切好处都是多余的——如果它们存在的话，那通常只会变成一种负担。只有这种人我们才可以说：他们的重心就在他们的自身当中。由此，我们可以解释清楚为何这类极其稀罕的人物，就算他们有着最良好的性格脾性，也不会对朋友、家庭和集体表现出其他人都会有的那种强烈的休戚与共的兴趣。他们拥有自身内在，那么，尽管失去了其他的一切也能得到安慰。因此，在他们身上有着一种孤独的特质；尤其在别人从来没有真正完全地满足过他们的时候，这种特质就更加明显。他们因而无法视别人为自己的同类。的确，当彼此的差异无处不在的时候，他们也就慢慢地习惯了作为另类的人生活在人群当中。在称呼人群时，他们脑子里想到的是第三人称的“他们”，而不是第一人称的“我们”。 

由此看来，那些在精神思想方面得到大自然异常慷慨馈赠的人，也就是最幸运的人了。确实，属于主体的东西比起属于客体的东西距离我们更近；如果客观事物真要发挥什么作用的话，无论其作用为何，那永远都是首先通过主体才能发挥作用。因此，客观事物只是第二性的。以下这些优美的诗句可以作证： 

 

> 真正的财富只能是灵魂的内在财富； 
>
> 其他别的东西带来烦恼多于好处。 
>
> ——卢奇安语 

 

一个具有丰富内在的人对于外在世界确实别无他求，除了这一具有否定性质的礼物——闲暇。他需要闲暇去培养和发展自己的精神才能，享受自己的内在财富。他的要求只是在自己的一生中，每天每时都可以成为自己。当一个人注定要把自己的精神印记留给整个人类，那么，对这个人就只有一种幸福或者一种不幸可言——那就是，能够完美发掘、修养和发挥自己的才能，得以完成自己的杰作。否则，如果受到阻挠而不能这样做，那就是他的不幸了。除此之外的其他别的东西对于他来说都是无关重要的。因此，我们看到各个时代的伟大精神人物都把闲暇视为最可宝贵的东西；因为闲暇之于每个人的价值是和这个人自身的价值对等的。“幸福好像就等同于闲暇”，亚里士多德这样说过。狄奥根尼斯告诉我们：“苏格拉底珍视闲暇甚于一切”。与这些说法不谋而合的是，亚里士多德把探究哲学的生活称为最幸福的生活。他在《政治学》里所说的话也跟我们的讨论相关联；他说：“能够不受阻碍地培养、发挥一个人的突出才能，不管这种才能是什么，是为真正的幸福。”歌德在《威廉·迈斯特》中的说法也与此相同：“谁要是生来就具备、生来就注定要发挥某种才能，那他就会在发挥这种才能中找到最美好的人生。”但拥有闲暇不仅对于人们的惯常命运是陌生的、稀有的，对于人们的惯常天性而言也是如此，因为人的天然命运就是他必须花费时间去获得他本人以及他的家人赖以生存的东西。人是匮乏的儿子，他并不是自由发挥思想的人。因此，闲暇很快就成了普通大众的包袱。的确，如果人们不能通过各种幻想的、虚假的目标，以各式游戏消遣和爱好来填塞时间，到最后，闲暇就会变成了痛苦。基于同样的原因，闲暇还会给人们带来危险，因为“当一个人无所事事的时候难以保持安静”是相当正确的。但是，在另一方面，一个人拥有超出常规配备的智力却也是反常的，亦即违反自然的。如果真的出现这样一个禀赋超常的人，那么，闲暇对于这一个人的幸福就是必不可少的——尽管闲暇对于他人来说只是一种负担和麻烦。因为缺少了闲暇，这种人就犹如被套上木轭子的柏加索斯那样闷闷不乐。但如果上述的两种特殊反常的情形碰巧结合在一起一拥有闲暇属于外在的特殊情形，而具有超常禀赋则是内在的反常情形——那就是一个人的一大幸运。因为这样的话，那个得天独厚的人现在就可以过上一种更加高级的生活，也就是说，这样的生活免除了人生两个对立的痛苦根源：匮乏和无聊。换句话说，他再不用为生存而忧心忡忡地奔忙，也不会无力忍受闲暇（闲暇也就是自由的生存）。人生这两种痛苦也只有通过它们的彼此抵消和中和，才使常人得以逃脱它们的困扰。 

虽然如此，我们却要考虑到：一个具有优异禀赋的人由于头脑超常的神经活动，对形形色色的痛苦的感受力被大大加强了。另外，他那激烈的气质——这是他拥有这些禀赋的前提条件——以及与此密切相关的对事物和形象的更加鲜明、完整的认识，所有这些都使被刺激起来的情绪更加强烈。一般而言，这些感觉情绪总是给这种人带来痛苦多于愉快。最后一点就是巨大的精神思想禀赋使拥有这些禀赋的人疏远了他人及其追求。因为自身的拥有越丰富，他在别人身上所能发现得到的就越少。大众引以为乐的、花样繁多的事情，在他眼里既乏味又
浅薄。那无处不在的事物均衡互补法则或许在这里也发挥着作用。确实，人们经常挂在嘴边的，并且似乎不无道理的说法就是：头脑至为狭窄、局促的人根本上就是最幸福的，虽然并没有人会羡慕他们的这一好运。我不想让读者先入为主，在这一问题上给予一个明确的说法，尤其是索福克勒斯本人在这一问题上就表达过两种互相矛盾的意见： 

> 头脑聪明对于一个人的幸福是主要的。 

又 

> 要过最轻松愉快的生活莫过于头脑简单。 

 

在圣经《旧约》里，贤哲们的说法同样令人莫衷一是： 

> 愚人的生活比死亡还要糟糕。
>
> 越有智慧，就越烦恼。 

 

在这里，我不会忽略提及这样的一类人：他们由于仅仅具备了那常规的、有限的智力配给，所以，他们并没有精神思想上的要求，他们也就是德语里的Philistine——“菲利斯坦人”。这名称源自于德国的大学生词汇。后来，这一名称有了更深一层的含义，虽然它和原来的意思依然相似；“菲利斯丁人”指的是和“缪斯的孩子”恰恰相反的意思，那就是“被文艺女神抛弃的人”。确实，从一个更高的角度审视，我应该把菲利斯丁人的定义确定为所有那些总是严肃古板地关注着那并非现实之现实的人。不过，这样一个超验的定义却跟大众的视角不相吻合——而我在这本书里所采用的就是大众的视角——所以，这样的定义或者不会被每一个读者所透彻理解。相比之下，这名称的第一个定义更加容易解释清楚，它也详细表现了菲利斯丁人的特质及其根源。因此，菲利斯丁人就是一个没有精神需求的人。根据我提及过的原则，“没有真正的需求也就没有真正的快乐”就可以推断：首先，对于他们的自身，菲利斯丁人并没有感受精神上的乐趣。他的存在并没有受到任何对知识的追求和对真理的探索这一强烈欲望的驱动，也没有要享受真正的美的热切愿望——美的享受与对知识、真理的追求密切相关。但如果时尚或者权威把这一类快乐强加给他们，那他们就会像应付强制性苦役般地尽快把它们打发了事。对这种人来说，真正的快乐只能是感官的快乐。牡蛎和香槟就是他们生存的最高境界。他们生活的目的也就是为自己获得所有能为他们带来身体上安逸和舒适的东西。如果这些事情把他们忙得晕头转向，那他们就的确快乐了！因为如果从一开始就把这些好东西大量提供给他们，他们就会不可避免地陷入无聊之中，而为了对抗无聊，他们是无所不用其极的：舞会、社交、看戏、玩牌、赌博、饮酒、旅行、马匹、女人等等。但所有这些都不足以赶走无聊，因为缺少了精神的需求，精神的快乐也就是不可能的。因此，菲利斯丁人都有一个奇异的特征，那就是：他们都有一副呆滞、干巴巴的类似于动物的一本正经和严肃表情。没有什么事情能使他们愉快、激动，能提起他们的兴趣。感官的乐趣很快就会烟消云散。由同样的菲利斯丁人所组成的社交聚会，很快就变得乏味无聊，纸牌游戏到最后也变得令人厌倦。不管怎样，这种人最终还剩下虚荣心。他们以各自不同的方式享受虚荣心所带给他们的乐趣，那就是：他们尽力在财富或者社会地位，或者权力和影响力方面胜人一筹，并藉此获得他人对自己的尊崇。又或者，他们至少可以追随那些拥有上述本事的人，以沐浴在这些人身上折射出来的光辉之中。从我们提到的这些菲利斯丁人的本质，可以引出第二点：对于他人，由于菲利斯丁人没有精神上的需求，而只有身体上的需要，所以，他们在与他人的交往中，会寻求那些能够满足自己身体上的需要，而不是精神上的需求的人。因此，在他们对别人的诸多要求当中，最不重要的就是一个人所具有的精神思想。当他看见别人具有突出的精神思想时，那反而只会引起他的反感，甚至憎恨。因为，他有着一股可憎的自卑感，以及呆笨的、不为人知的嫉妒心——他小心翼翼地试图把它们掩饰起来，甚至对自己也是这样。但这样一来，这种嫉妒有时候就会变成某种私下里的苦涩和愤怒。因此，他永远也不会想到要对卓越的精神思想给予恰如其分的尊崇和敬意；他一心一意地把尊崇和敬意留给拥有地位、财富、权力、影响的人，因为这些东西在他的眼中才是真正优越的东西。在这些方面出风头也就成了他的愿望。所有这一切都源于这一事实：他是一个没有精神需求的人。 

菲利斯丁人的巨大痛苦就在于任何理念性的东西都无法带给他们愉快。他们为了逃避无聊，不断需要现实性的事物。但由于现实性的东西很快就会被穷尽，一旦这样，它们就不但不再提供快乐，反而会使人厌烦。并且，这些东西还会带来各种祸殃。相比较而言，理念性的东西却是不可穷尽的，它们本身既无邪也无害。 


在关于何种个人素质、禀赋能给人带来幸福的所有这些讨论中，我关注的主要是人的体质和智力上的素质，至于人的道德素质以何种方式直接地给人以幸福——这问题我在我的关于道德的基础的获奖论文里面已经谈论过了。因此，我推荐读者阅读那篇论文。 

 


## 人所拥有的财产 

伟大的幸福论教育家伊壁鸠鲁正确而美妙地把人的需要划分成为三类。第一类属于人的天然的和迫切的需要。这类需要如果得不到满足，就会造成人的痛苦。顺理成章这一类需要也就是食品和衣物，它们比较容易得到满足。第二类需要同样是天然的，但却不是迫切的。那就是满足性欲的需要，尽管伊壁鸠鲁在《赖阿特斯的报道》中没有把它说出来（在这里我把他的学说表达得更清楚、更完整）。要满足这一类需要就相对困难一些了。第三类的需要则既不是天然的，也不是迫切的，那就是对奢侈、排场、铺张和辉煌的追求。这些需要没有止境，要满足这些需要，也是非常困难的。 

在拥有财产的问题上，要给我们合乎理智的愿望界定一个限度，如果不是不可能，那也是一件很困难的事情，因为一个人在拥有财产方面能否得到满足并不由某一个财产的绝对数量所决定。这其实取决于一个相对的数量，也就是说，由一个人所期待得到的财产和自己已经实际拥有的之间的关系决定。因此，仅仅考察一个人的实际拥有毫无意义，这种情形就犹如在计算一个分数时，只计算分子而忽略了分母一样。当对某一样东西的要求还没有进入一个人的意识的时候，这个人完全不会感觉到对它有所欠缺。没有这样东西，他照样心安理得。但一个拥有百倍以上财产的人，只要他对某样东西产生了要求，而又得不到它，那他就会感到怏怏不乐。在这一方面，对于一些他认为有可能得到满足的要求，每个人都有他的视线范围。他的要求不会超出这一视线范围。处于他心目中的视线范围之内的具体之物一旦出现，而他又确信能够得到它，那他就会感到幸福。但是如果得到这具体之物存在重重困难，他根本就没有得到它的希望和可能，那他就会感觉不幸和痛苦。所有在他视线以外的东西，都不会对他产生任何影响。因此，穷人不会因为得不到巨大的财富而焦虑不安，但富人在计划失算落空的时候，不会考虑到自己已经拥有相当可观的财物，并以此安慰自己。财富犹如海水：一个人海水喝得越多，他就越感到口渴。这一道理同样适用于名声。我们在失去了财富或者安逸的处境以后，当我们挺住了最初的阵痛，我们惯常的心境与当初相比较，并没有发生很大的改变——这是因为：当命运减少了我们的财富以后，我们自己也就相应降低了我们的要求。在遭遇不幸时，上述过程的确是痛苦方分的；但这个过程完成以后，痛苦也就减少许多了，到最后甚至感觉不到了，因为伤口已经愈合了。反过来，如果交到好运，我们的期望的压缩机就会把期望膨胀起来，我们在这过程中就感受到了快乐。但是，这一欢乐并不会维持长久。当整个过程全部完成以后，那扩大了的要求范围已经被我们习以为常了；并且，与新的要求相比较，我们就会对目前的拥有不以为然了。荷马在《奥德赛》的第十八节表达了我这里所说的意思。这一节最后的两行是这样的： 



> 凡夫俗子的情绪飘忽不定，
>
> 就像神、人之父所赐予的日子。 

 

我们之所以感到不满，原因就在于我们不断试图提高我们的要求，但同时，其他妨碍我们成功的条件因素却保持不变。 

对于像人类这样一个贫乏不堪、充满需求的物种，财富比起任何其他别的东西都得到人们更多的和更真诚的尊重，甚至崇拜，这是毫不奇怪的。甚至权力本身也只是获取财富的工具。不足为奇的还有：为了达到获取财富这一目的，一切尽可以抛开，一切都可以推翻。例如，在哲学教授手中的哲学就落得了这样的下场。 

人们的愿望首先指向了金钱，人们热爱金钱甚于一切，人们经常为此受到责备。但是，人们热爱金钱却是自然的，甚至是不可避免的。金钱就像永远不知疲倦的普鲁特斯，每时每刻都准备着变成我们那飘忽不定的愿望和变化多端的需要所要求的物品。任何其他物品只能满足一个需要，诸如食物之于饥饿的人，醇酒之于健康者，药物之于病人，皮毛之于冬季，女人之于小伙子等等。因此，它们都只是“服务于某一特定的东西”，它们的好处是相对的。唯独金钱才具备了绝对的好处。因为它并不只是满足某一具体的需要，而是满足抽象中的普遍
的多种需要。 

我们应把手头上的财富视为能够抵御众多可能发生的不幸和灾祸的城墙，这些财富并不是一纸任由我们寻欢作乐的许可证，花天酒地也不是我们的义务。如果一个人凭藉自己的某种天赋才能——不管这种才能是什么——从最初的一文不名到最终赚到可观的金钱，那他就会错觉地认为：自己的天赋才能是恒久不变的本金，他以此赚取的金钱只是本金的利息而已。因此，他不会把挣来的一部分金钱积累成为固定长久的本金，而是把挣来的钱随手花掉。这样，他们通常最终陷入贫困，因为如果他们的才能只能维持短暂的时间，例如：几乎所有从事优美艺术的人都属于这一类情况，那么，他们的天赋才能就有枯竭、耗尽的时候。又或者，他们挣钱的本事依赖某种环境和某种风气。这种环境、风气随后消失了，这样，他们的钱财收入也就停止了。手工制作者尽可以像我上面所说的那样花钱大手大脚，财来财去，因为他们不会轻易失去制作才能，他们也不会被助手、帮工的力气所替代。并且，他们的产品是大众需求的对象，所以不愁找不到销路。因此，这一说法是正确的：“掌握一门手艺，就是拿到了一个金饭碗。”各种类型的艺人和艺术家遭遇的情形却不一样。正因为这样，他们获取的
报酬是如此的优厚。他们所挣得的金钱因此应该变成他们的本金。但他们却把挣来的金钱只当作利息。这样，他们就走向了贫穷的结局。相比之下，继承了财产的人起码立刻就正确地认识到何为本金、何为利息。所以，他们之中的大多数人会尽力稳妥地维护自己的本金。事实上，如果可能的话，他们至少会把利息的八分之一存起来以应付将来的需要。因此，他们大多数人都生活得充裕、富足。我这里所说的并不适用于商人，因为对商人来说金钱本身就是挣取更多金钱的手段，是他们生财的工具。因此，尽管金钱是他们以汗水换来的，但他们仍然会试图以最佳的方式运用这些金钱，以保存和增加其资本。因此，这些人比起任何别的阶层的人都更懂得巧妙、适宜地运用金钱。 

在一般的情况下，那些经历过匮乏和贫穷的人，比较不那么害怕贫困，因此更加倾向于奢侈豪华。这是比较那些只是听说过贫困的人而言的。前者包括那些交上了某种好运，或者，得益于自己拥有的某一专门的特长——不论这特长是什么——从当初的贫困迅速达到了小康生活的人；后者包括出生并成长于良好家境的人。后者更加着眼于未来，因此他们比起前者过着更加节俭的生活。由此，我们可以得出结论：贫穷并不像我们所粗略看到的那样糟糕。不过在这一例子里，真正的原因或许是那些出生于富有家庭的人把财富视为必不可少，是构成唯一可能的生活的元素，就像空气般的不可或缺。因此他们就像保护自己的生命一样警觉地保护自己的财产。所以他们通常都有条不紊、小心谨慎、勤俭节约。相比之下，出生于世代贫困之家的人却把贫穷视为理所当然的事情。他们所继承得到的财富对于他们来说只是一种多余的东西，把财富用作享受或挥霍才够合适！一旦把钱财耗尽，他们仍然像以前没钱的时候那样生活下去，并且，还免除了一样烦恼哩！这就像莎士比亚说的那样： 

 

> 乞丐一旦跨上了坐骑，就非得把马跑死为止。 
>
> ——《亨利五世》 

 

当然，这种人对自己的运气和能力都抱有坚定的和过分的信心，因为这两者都帮助他们脱离了贫困的境地。不过，他们的信心更多地是在他们的心里，而不是在他们的头脑里。因为他们和那些出身富裕的人并不一样，他们并没有把贫困视为一个无底深潭。他们认为，只要脚踏实地用力蹬上几脚，就能重新浮上水面。这一人性的特征可以解释为何出身贫穷的女子，比起为夫家带来丰厚嫁妆的富家女，通常更加挑剔、讲究和更加奢侈、挥霍，因为在大多数的情况下，富家出身的女子不仅仅带来了钱财；她们比起穷家女还有着一种更为热切的、得之于遗传的保护财产的愿望。不过，谁要是对此持有相反的意见，那他可以在阿里奥斯图的第一首讽刺作品里找到支持他的观点的权威说法。但约翰逊博士却赞同我的意见：“一个习惯于处理钱财的有钱女人，会小心翼翼地花钱。但一个在结婚以后才首次获得支配金钱权力的女人，会在用钱的时候大胆妄为，她简直就是大肆挥霍。”（《约翰逊的一生》，博斯威尔著）不管怎么样，我都要奉劝那些娶贫穷女子为妻的人不要让她们继承本金，而只是领取一份年金。他们尤其需要注意，不要把孩子的财产交到她们的手上。 

我在这里提醒人们谨慎保存挣来的或者继承下来的财产。我相信这样做并没有用我的笔写了些毫无价值的东西。如果一个人从一开始就拥有足够的财产，能够享有真正的独立自足，也就是说，可以不用操劳就能维持舒适的生活——甚至只够维持本人而不包括他的家人就行——那就是一种弥足珍贵的优越条件；因为这个人就能以此摆脱纠缠人生的匮乏和操劳，他也就从大众的苦役中获得了解放——而这苦役本是凡夫俗子的天然命运。只有得到命运如此垂青和眷顾的人，才是真正自由的人。这样的人才成为自己的主人，是自己的时间和自己的力量的主宰。每天早晨他就可以说上一句：“今天是属于我的”。因此原因，一个拥有一千塔勒年金的人与一个拥有十万塔勒年金的人相比较，两者之间的差别远远少于前者与一个一无所有的人之间的差别。如果祖传的家产落到一个具备高级精神禀赋的人的手里——这个人所要从事的事业跟埋头挣钱并不怎么对得上号——那么，这笔遗产就能发挥出它的最高价值，因为现在这个人受到了命运的双重馈赠，他尽可以为自己的天才而生活了。他能够从事别人无法从事的事情，创造出对大众都有益处，且又能给自己带来荣耀的东西。他以这种方式百倍地偿还自己欠下世人的债务。处于同样优越生活条件的其他人则可以通过从事慈善活动为人类作出贡献。相比之下，如果一个人继承了遗产，但却又不曾做出任何上述事情——哪怕他只是尝试这样做，或者只是做出了点滴的成绩——或者，他甚至没有试图细致地研究某一门学问，以支持和推动这门学问的发展；那么，这样的人就只是一个可耻的无所事事者。这种人也不会感到幸福，因为免除了贫穷只会把他引至人生的另一个痛苦极端——无聊。他受尽无聊的百般折磨。假如贫穷的处境使他有事可做的话，他反倒会生活得更加幸福。百无聊赖、无所事事很快就会把他引向奢侈挥霍，由此他就被剥夺了他那不配享受的优越条件。许多有钱人到最后沦为贫困，就是由于有钱
就挥霍殆尽，目的只不过是为了从压迫他们的无聊那里谋求片刻的喘息。 

但如果我们的目标是要在公职服务中达至高位，那就是完全另一回事了，因为为此目标我们必须赢得朋友、关系和受到别人的青睐；只能以此方式获得逐级晋升直至最高职位。这样，从根本上来说，一文不名地来到这个世界反而更好。尤其这个人没有显赫高贵的出身，但却具备了一定的才能。如果这个人是一个一无所有的穷光蛋，那反倒是他的一个真正优势，他也可因此获得别人的提携。因为每个人喜欢和寻找的就是别人的缺点和不足——这在人与人之间的谈话里面已经如此，在国家公务事业方面情况就更是这样。只有一个穷鬼才会对自己绝对的、彻底的、全方位的劣势达到所需要的深信不疑的程度，才会认识清楚自己的无足轻重和毫无价值。只有在这种情况下，这种人才会接连不停地向人弯腰致意，也只有他们的鞠躬才会深至九十度。只有这种人才能忍受一切，且一直报以微笑。只有他们才知道自己的奉献是完全没有价值的；只有他们才会扯高嗓门，或者用醒目的黑体字，公开把拙劣的文字作品捧为巨著——那些作者不是高高在他们之上，就是极有势力；也只有这种人才会摇尾乞怜。因此，只有他们才会在青年时期就已成为倡导下面这一不为人知的真理的人——这一真理由歌德通过这些字句向我们展示了出来： 

 

> 任何人都不要抱怨卑鄙和下流，因为 
>
> 在这世上只有卑鄙和下流才是威力无比的。 

 

相比之下，从一开始就生活无忧的人，却大多难以管束。他们习惯于高视阔步，并不曾学会上述为人处世的艺术。或许他们具有某样能引以为傲的才能，但他们应该认识到这些才能与平凡庸俗、溜须拍马根本无法匹敌。最终，他们会看到身居比自己更高位置的人的平庸和低劣之处。此外，如果他们还遭受别人的侮辱和种种令人愤慨的事情，他们就会羞愧、茫然和害怕。这可不是在这个世界上生存的办法。相反，他们应该和勇敢的伏尔泰一道说出这样的话：“我们在这世上时日不多，不值得在可鄙的坏蛋的脚下爬行。”随便说上一句，令人遗憾
的是“可鄙的坏蛋”这一词可适用于这世上的很多人。因此，我们可以看到尤维纳利斯的诗句：

 

> 在局促狭窄的屋子里，无从施展， 
>
> 要昂首挺胸已经非常困难。 

 

更适用于艺术表演的职业，而不大适用于其他世俗、钻营的人们。 

在“人所拥有的财产”这一章里，我并没有把妻子和儿女包括其中，因为与其说一个人拥有妻子、儿女，还不如说妻子、儿女拥有他。朋友反倒更应该被划入一个人的拥有物里面，但甚至在这问题上，拥有者也还是在某种程度上成为别人的拥有物。 
"""

    summary = auto_summary(sample)

    assert isinstance(summary, list)

