'''В Santa Claus Headquarters, Лапландия, този декември има проблеми с телевизията. Рудолф, при едно от кацанията си,
повреди антената за телевизията и сега джуджетата имат достъп само до Лапландската Национална Телевизия, която обаче не излъчва спорт.
А елфите обичат да гледат тенис и нямат търпение за финалния турнир от календара.
Тъй като Дядо Коледа не позволява използването на SnowVPN за да бъдат гледани мачовете онлайн,
то джуджетата имат една единствена опция - отделни push нотификации, които казват кой е спечелил последната изиграна точка от мача.
Джуджетата знаят правилата за точкуване в тениса,
така че нямат проблеми да следят ситуацията. Едно от джуджетата, обаче, предпочита да продължава с работата си и да прави играчки, вместо да "гледа" тенис в работно време.
 Той все пак иска да знае кой е спечелил мача, затова вие трябва да напишете програма, която му казва кой е победителя.

А ето и правилата за точкуване:

Един мач се състои от няколко сета, всеки сет – от няколко гейма, а всеки гейм – от няколко разигравания. Най-честият формат на игра е "2 от 3" сета.
При него, играчът, който спечели 2 сета (независимо колко до сега е спечелил опонентът му) печели мигновено.
 Това означава, че всеки пълен мач (в който никой от играчите не се е отказал) в този формат се състои или от 2, или от 3 сета.

Геймове В началото на всеки гейм и двамата играчи са с по нула точки (0:0). Всяко разиграване носи определен брой точки на играча, който го спечели.
 Първото и второто спечелено разиграване носят по 15 точки, третото 10, а от четвъртото - победа, освен ако резултатът не е 40:40.
 Например, ако първият играч е спечелил едно разиграване, а вторият – три, резултатът би бил 15:40. Ако и двамата са спечелили по две, би бил 30:30.
  Ако първият е спечелил три, а вторият 0, ще е 40:0. Ако първият е спечелил 4, а вторият 2, резултат няма да има, тъй като първият ще е спечелил гейма.


В случай, че играчите достигнат 40:40, започват да играят докато единият от двамата поведе с две спечелени разигравания.
По-точно, в началото са "равни" (deuce), а когато някой спечели разиграване, почва да "води" (advantage).
 Ако спечели още едно разиграване веднага, той печели гейма. Ако пък противникът му спечели разиграването, отново стават "равни".
 Забележете, че тези правила не важат, ако геймът е тайбрейк (описан по-долу).

Сетове Всеки сет се играе докато някой от играчите не спечели 6 гейма, но има допълнително изискване да води с поне два такива.
Тоест, валидни резултати, в които единият от играчите е спечелил сета, са 1:6, 6:4, 3:6, докато такива, които все още не са завършили, са 6:5 или 5:6.
В този случай се играе още един гейм. Ако резултатът стане 5:7 или 7:5, играчът, който е станал 7, печели сета.
Ако, обаче, стане 6:6 се играе още един "специален" гейм, наречен тайбрейк ("tiebreak")

Тайбрейк В специалния гейм, наричан тайбрейк, се играе до 7 спечелени разигравания, като отново има изискване победителят да има преднина поне две.
Тоест валидни завършили тайбреци са 7:1, 3:7, 5:7, 7:5, но не и 7:6 или 6:7, тъй като преднината е само едно разиграване.
 В този случай се продължава, докато някой от играчите не достигне до преднина от две спечелени разигравания.

Input Format

На първия ред на стандартния вход ще бъде зададено едно цяло число N – колко разигравания е имало в целия мач.
На всеки от следващите N реда ще има по един низ от главни и малки латински букви Si – фамилията на някой от играчите.
 Гарантирано е, че фамилиите на играчите ще са различни и ще има само два уникални стринга сред дадените N.
  Също така е гарантирано, че мачовете са валидни – всъщност, за тестове са използвани логове от реални мачове!
  Гарантирано е също така, че в никой от избраните мачове няма отказал се играч – тоест, мачовете са изиграни изцяло.
  Всички мачове са във формат "2 от 3".

Constraints

Output Format

На единствен ред на стандартния изход изведете един единствен стринг – фамилията на победителя в мача.

Sample Input 0

72
Nadal
Nadal
Nadal
Montanes
Nadal
Montanes
Nadal
Nadal
Nadal
Montanes
Nadal
Nadal
Montanes
Montanes
Nadal
Nadal
Nadal
Nadal
Nadal
Nadal
Montanes
Montanes
Nadal
Nadal
Nadal
Nadal
Montanes
Montanes
Nadal
Nadal
Montanes
Montanes
Montanes
Montanes
Nadal
Montanes
Nadal
Nadal
Nadal
Nadal
Nadal
Montanes
Montanes
Nadal
Montanes
Nadal
Nadal
Nadal
Nadal
Nadal
Nadal
Montanes
Montanes
Nadal
Nadal
Nadal
Nadal
Nadal
Nadal
Montanes
Nadal
Nadal
Nadal
Montanes
Nadal
Nadal
Nadal
Nadal
Montanes
Nadal
Nadal
Nadal

Sample Output 0

Nadal

'''


n_plays = int(input())
for play in range(n_plays):
    player = input()
    if play == n_plays-1:
        print(player)

