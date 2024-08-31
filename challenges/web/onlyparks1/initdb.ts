import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

const CLOWNS = [
  {
    name: "Bubbles",
    email: "bubbles@clownmail.com",
    password: process.env.FLAG || "flag-placeholder",
    isAdmin: true,
  },
  {
    name: "Giggles",
    email: "giggles@clownmail.com",
    password: "RedNose123",
    isAdmin: false,
  },
  {
    name: "Chuckles",
    email: "chuckles@clownmail.com",
    password: "FunnyShoes!",
    isAdmin: false,
  },
];

const ARTICLES = [
  {
    title: `Un tourbillon de rires et de frissons à La Ronde`,
    body: `<p>Salut les amis! Ici Bubble, votre clown préféré, prêt à vous emmener dans un voyage haut en couleurs à travers La Ronde, le parc d'attractions où les rires sont aussi nombreux que les montées d'adrénaline! 🎈</p>

<h1>Une journée pas comme les autres</h1>
<p>Dès que vous franchissez les portes de La Ronde, c’est comme si vous entriez dans un monde magique où tout est possible. Des manèges qui défient la gravité, des friandises sucrées qui fondent dans la bouche, et des spectacles qui font briller les yeux des petits et des grands – voilà le genre de journée qui vous attend!</p>

<h1>Les montagnes russes : frissons garantis!</h1>
<p>Parlons un peu de ce qui fait battre le cœur à La Ronde : les montagnes russes! Si vous avez le goût du risque, direction le Goliath, cette bête d'acier qui vous propulse à des vitesses folles. Vous aurez l’impression de voler comme un oiseau (ou un clown dans un canon!) en atteignant des sommets vertigineux.</p>
<p>Mais ne vous inquiétez pas si vous n’êtes pas un casse-cou, il y en a pour tous les goûts! Les plus jeunes (et les clowns moins courageux) adoreront le Dragon, une montagne russe plus douce mais tout aussi amusante. Peu importe votre choix, vous repartirez avec des souvenirs inoubliables… et peut-être quelques mèches de cheveux en moins après tous ces cris!</p>

<h1>Des spectacles qui éclatent de rire</h1>
<p>Si les manèges ne sont pas votre tasse de thé, La Ronde offre aussi une variété de spectacles qui valent le détour. Qu’il s’agisse de cascades impressionnantes, de concerts endiablés, ou de parades colorées, il y a toujours quelque chose pour vous faire taper des mains et rire aux éclats.</p>
<p>Et devinez quoi? Moi, Bubble, je me suis même produit sur scène! Imaginez un instant : un clown essayant de jongler tout en gardant son chapeau sur la tête dans le vent de Montréal… pas facile, mais oh combien drôle!</p>

<h1>Des délices sucrés pour reprendre des forces</h1>
<p>Après tant d’émotions, il est temps de faire une pause gourmande. Les kiosques de La Ronde regorgent de friandises qui vous mettront l’eau à la bouche. Des barbes à papa roses et moelleuses, des pommes d'amour sucrées, et bien sûr, des cornes d'abondance de pop-corn croustillant. Miam! De quoi redonner de l’énergie à n’importe quel clown en fin de journée.</p>

<h1>En conclusion : un monde merveilleux</h1>
<p>La Ronde, c'est bien plus qu'un simple parc d'attractions. C'est un lieu où l'on crée des souvenirs, où les familles se rapprochent, et où les clowns comme moi trouvent leur bonheur à chaque coin de rue. Que vous soyez un amateur de sensations fortes, un gourmand invétéré, ou simplement à la recherche d'une journée de divertissement sans fin, La Ronde est l'endroit parfait pour laisser parler l'enfant qui est en vous.</p>

<p>Alors, enfilez vos plus belles chaussures (même si elles sont un peu trop grandes!), et venez vivre l'aventure de votre vie à La Ronde. Et si vous croisez un clown nommé Bubble en train de faire des grimaces ou de jongler avec des glaces, n’oubliez pas de lui faire un coucou!</p>

<p>À bientôt, les amis! Et surtout, n’oubliez pas : là où il y a des rires, Bubble n'est jamais loin! 🎪🎉</p>`,
    clownIds: [0],
  },
  {
    title:
      "Village Vacances Valcartier : Le paradis des clowns et des éclaboussures!",
    body: `<p>Salut à tous, c'est encore moi, Bubble, votre clown farfelu préféré, prêt à vous raconter ma journée inoubliable au Village Vacances Valcartier! Préparez vos bouées, car ici, c’est la fête des éclaboussures et des glissades folles! 🌊🎈</p>

<h1>Une arrivée en fanfare... et en maillot!</h1>
<p>Dès que je suis arrivé au Village Vacances Valcartier, j'ai tout de suite su que j’étais au bon endroit. Imaginez un peu : des piscines, des rivières paresseuses, et des toboggans géants qui semblent toucher le ciel! Moi, Bubble, j'ai enfilé mon plus beau maillot à pois multicolores et j'étais prêt à plonger dans l'aventure!</p>

<h1>Les glissades d'eau : rire et sensations garantis</h1>
<p>La première chose que j'ai fait, c'est de foncer vers les glissades d'eau. Et laissez-moi vous dire que celles du Village Vacances Valcartier sont vraiment hors du commun! Prenez le Turbo 6, par exemple. C'est une course endiablée sur des tapis où l'on file à toute allure. J'ai peut-être même réussi à devancer quelques enfants... mais chuuut, ne leur dites pas!</p>
<p>Pour ceux qui aiment les sensations fortes, le Himalaya et le Everest sont des incontournables. Ces deux toboggans gigantesques vous feront hurler de joie tout le long de la descente. Et moi, Bubble, j’ai dû vérifier que mon nez rouge était bien en place après avoir dévalé ces montagnes d’eau!</p>

<h1>Une rivière pas si tranquille que ça...</h1>
<p>Après tant d’émotions, j'ai voulu me détendre un peu dans la rivière d'aventure Amazon. Mais attention, ce n’est pas une rivière tranquille! Entre les courants, les vagues, et les surprises aquatiques, j'ai passé mon temps à éclater de rire et à éclabousser tout le monde autour de moi. Parfait pour un clown qui adore faire des vagues!</p>

<h1>Le royaume des enfants (et des clowns!)</h1>
<p>Le Village Vacances Valcartier, c’est aussi le paradis des petits clowns en herbe. Le Mirage et le Repaire des Pirates sont des aires de jeux aquatiques où les enfants peuvent glisser, grimper, et s’amuser comme des fous. Bien sûr, moi aussi je me suis invité à la fête! Après tout, qui peut résister à une bataille d’eau contre des pirates?</p>

<h1>Un petit tour au Bora Parc</h1>
<p>Mais attendez, ce n’est pas tout! Le Village Vacances Valcartier a aussi son propre parc intérieur, le Bora Parc. Imaginez une plage tropicale, avec des palmiers, des piscines à vagues, et des glissades d'eau… tout ça, à l'intérieur! Parfait pour continuer de s’amuser même quand la météo à l’extérieur n’est pas de notre côté.</p>

<h1>Des délices pour les gourmands</h1>
<p>Après toutes ces aventures, il fallait bien que je reprenne des forces. Et croyez-moi, au Village Vacances Valcartier, on sait comment faire plaisir aux gourmands! Entre les poutines bien garnies, les hot-dogs juteux, et les glaces colorées, mon ventre de clown était bien content.</p>

<h1>En conclusion : une aventure aquatique mémorable</h1>
<p>Le Village Vacances Valcartier, c’est l’endroit rêvé pour une journée pleine de rires, d’éclaboussures, et de souvenirs inoubliables. Que vous soyez un amateur de glissades d’eau, un explorateur des rivières, ou un petit clown en quête de nouvelles aventures, il y a quelque chose pour tout le monde ici.</p>

<p>Alors, si vous cherchez une escapade aquatique où le plaisir ne s’arrête jamais, enfilez votre maillot, attrapez votre bouée, et rejoignez-moi au Village Vacances Valcartier. Et n’oubliez pas : où il y a de l’eau et des rires, Bubble n'est jamais loin! 🌟💦</p>

<p>À bientôt, mes amis mouillés!</p>`,
    clownIds: [0],
  },
  {
    title: "Parc Safari : Une aventure sauvage avec Bubble le clown!",
    body: `<p>Salut les amis, c’est Bubble, votre clown toujours prêt pour une nouvelle aventure! Aujourd’hui, je vous emmène faire un tour au Parc Safari, où les animaux sont les stars et les rires résonnent à chaque coin. Accrochez-vous bien, car cette journée au cœur de la savane québécoise est pleine de surprises! 🦁🎪</p>

<h1>Une entrée sauvage et souriante</h1>
<p>Dès que vous franchissez les portes du Parc Safari, vous êtes accueilli par un air de jungle et un concert de rugissements, de barrissements et de cris d’oiseaux exotiques. Moi, Bubble, j’étais tellement excité que mon chapeau a failli s’envoler! Pas de panique, je l’ai rattrapé juste à temps avant de sauter dans le Safari Aventure.</p>

<h1>Safari Aventure : Rencontres inoubliables</h1>
<p>Le Safari Aventure, c’est un peu comme un tour du monde en quelques kilomètres. Vous montez à bord de votre voiture ou du petit train, et hop, vous partez à la rencontre des lions, des girafes, des zèbres et même des éléphants! Je vous le dis, voir un lion de si près, ça fait battre le cœur, même pour un clown habitué aux acrobaties!</p>
<p>Et devinez quoi? Les animaux viennent parfois si près qu’on pourrait presque leur serrer la patte (mais on ne le fait pas, bien sûr!). C’est une expérience magique que je n’oublierai jamais. Les girafes sont tellement curieuses qu’elles ont même essayé de goûter mon nez rouge. Quelle coquine!</p>

<h1>Le Tunnel des Lions : Un face-à-face rugissant</h1>
<p>Ensuite, direction le Tunnel des Lions. Imaginez-vous dans un tunnel de verre, entouré de majestueux lions qui se prélassent au-dessus de votre tête. Moi, Bubble, j’ai essayé de faire mon plus beau rugissement pour leur dire bonjour… mais je crois que je leur ai juste donné envie de faire une petite sieste. Ah, la vie de lion!</p>

<h1>La promenade Safari</h1>
<p>Après tant d’émotions, une petite balade s’impose. La promenade Safari vous permet de marcher parmi les kangourous, les lémuriens, et les perroquets. Ici, c’est le royaume des animaux curieux et joueurs, parfait pour un clown qui aime autant s’amuser. J’ai même tenté de faire la course avec un lémurien… bon, disons qu’il était un peu plus rapide que moi, mais l’important, c’est de participer, non?</p>

<h1>Les jeux d'eau du Safari</h1>
<p>Le Parc Safari, c’est aussi un endroit parfait pour se rafraîchir! Après avoir exploré la savane, quoi de mieux qu’une bonne éclaboussure dans les jeux d’eau? Les enfants adorent, et moi aussi! Rien de tel que de courir sous les jets d’eau, de glisser sur les toboggans et de se laisser emporter par les rires. Même les éléphants seraient jaloux de ces éclaboussures!</p>

<h1>Des souvenirs pour tous</h1>
<p>Avant de repartir, j’ai fait un petit tour à la boutique de souvenirs. Entre les peluches d’animaux, les chapeaux de safari, et les t-shirts colorés, j’ai trouvé de quoi ramener un peu de cette journée magique avec moi. Et bien sûr, j’ai pris une petite peluche de lion pour me rappeler de cette rencontre inoubliable.</p>

<h1>En conclusion : Une journée sauvage et magique</h1>
<p>Le Parc Safari, c’est bien plus qu’un simple parc d’attractions. C’est une aventure qui vous emmène au cœur de la nature, où chaque moment est rempli de découvertes et de rires. Que vous soyez un amoureux des animaux, un explorateur en herbe, ou un clown toujours à la recherche de nouvelles aventures, ce parc est un endroit unique où les rêves deviennent réalité.</p>

<p>Alors, enfilez votre chapeau de safari, venez rugir de plaisir avec moi, Bubble, et découvrez le monde merveilleux du Parc Safari. Et rappelez-vous : là où il y a des animaux et des sourires, Bubble n'est jamais loin! 🦓🎉</p>

<p>À bientôt pour une nouvelle aventure sauvage, mes amis!</p>`,
    clownIds: [0],
  },
  {
    title: "Plongez dans le fun avec Giggles au Village Vacances Valcartier!",
    body: `<p>Salut les amis! C’est Giggles, le clown toujours prêt pour une bonne dose de rigolade et d’aventure! Aujourd’hui, je vous emmène dans un endroit où l’eau, les éclaboussures, et les rires sont à l’honneur : le Village Vacances Valcartier. Attrapez vos maillots, on plonge tout de suite dans le vif du sujet! 💦🎪</p>

<h1>Une entrée en fanfare... et en éclaboussures!</h1>
<p>Dès mon arrivée au Village Vacances Valcartier, j’ai su que j’étais au paradis des clowns qui adorent l’eau! Des piscines partout, des toboggans géants qui serpentent comme des serpents farceurs, et des enfants qui courent avec des sourires aussi grands que ceux de Giggles! J’ai rapidement enfilé mon maillot à pois colorés et me suis jeté à l’eau!</p>

<h1>Les glissades d'eau : Des descentes à toute vitesse</h1>
<p>Le premier arrêt? Les glissades d'eau, bien sûr! Le Turbo 6 m’a tout de suite attiré. C’est une course folle sur des tapis où l’on file à toute allure! J’ai essayé de battre les enfants à la course… mais disons que mes grandes chaussures de clown ne sont pas idéales pour ça. Mais l’important, c’est de rigoler, non?</p>
<p>Pour les amateurs de sensations fortes, les Everest et Himalaya sont un must! Ces toboggans géants m’ont fait hurler de plaisir tout en descendant à une vitesse folle. Je crois bien que mon chapeau de clown a fait deux tours avant de retomber sur ma tête!</p>

<h1>La rivière d'aventure : Un moment de détente... ou presque!</h1>
<p>Après tant d’émotions, j’ai voulu me détendre un peu dans la Rivière Aventure. Mais attention, ce n’est pas une rivière calme comme on pourrait le penser! Entre les courants, les vagues, et les surprises aquatiques, j’ai passé mon temps à éclater de rire et à essayer de garder mon équilibre sur ma bouée. Heureusement que Giggles sait toujours retomber sur ses pieds… ou presque!</p>

<h1>Le royaume des enfants : Où les petits deviennent des grands clowns!</h1>
<p>Le Village Vacances Valcartier, c’est aussi un terrain de jeu géant pour les petits (et les clowns aussi!). Le Mirage et le Repaire des Pirates sont des zones où les enfants peuvent grimper, glisser, et s’amuser sans fin. Moi, Giggles, je me suis bien sûr incrusté pour une petite bataille d’eau avec les pirates… et j’ai fini tout trempé mais avec un sourire jusqu’aux oreilles!</p>

<h1>Bora Parc : Une escapade tropicale</h1>
<p>Et devinez quoi? Même quand il fait frisquet dehors, le Village Vacances Valcartier a de quoi nous réchauffer avec le Bora Parc, son parc aquatique intérieur! Imaginez une plage tropicale, des palmiers, des piscines à vagues… tout ça sous un toit! Je me suis cru sur une île paradisiaque, avec en prime des glissades d'eau qui n’attendent que nous pour s’amuser.</p>

<h1>Des délices pour les gourmands</h1>
<p>Après tant d’aventures, une petite pause gourmande s’imposait. Au Village Vacances Valcartier, les kiosques regorgent de délicieux snacks pour les gourmands comme moi. Poutine bien garnie, hot-dogs et glaces colorées… il y avait de quoi faire briller mes yeux de clown!

<h1>En conclusion : Une journée mémorable et éclaboussée de rire</h1>
<p>Le Village Vacances Valcartier, c’est bien plus qu’un simple parc aquatique. C’est un endroit où l’on rit, où l’on s’éclabousse, et où l’on crée des souvenirs inoubliables. Que vous soyez un amateur de glissades d’eau, un explorateur en herbe, ou simplement à la recherche d’un moment de pure détente, ce parc a tout ce qu’il faut pour vous faire sourire.</p>

<p>Alors, enfilez votre maillot, attrapez une bouée, et rejoignez-moi, Giggles, pour une journée inoubliable au Village Vacances Valcartier. Et n’oubliez pas : là où il y a des éclaboussures et des rires, Giggles est toujours dans les parages! 🎉💦</p>

<p>À très bientôt pour une nouvelle aventure aquatique et pleine de rigolades!</p>`,
    clownIds: [1],
  },
  {
    title: "Une journée pleine de rires au Parc Safari avec Giggles le clown!",
    body: `<p>Bonjour à tous, ici Giggles, le clown toujours prêt à faire sourire petits et grands! Aujourd'hui, je vous emmène dans une aventure sauvage au Parc Safari. Attachez vos ceintures et préparez-vous pour une journée où les animaux et les éclats de rire sont les rois! 🦁🎈</p>

<h1>Le début d'une aventure sauvage</h1>
<p>Dès que vous franchissez les portes du Parc Safari, vous êtes transporté dans un monde où les animaux règnent en maîtres. Moi, Giggles, j’étais tellement excité que mes chaussures de clown ont commencé à sautiller toutes seules! C’est parti pour une journée pleine de découvertes et d’amusement!</p>

<h1>Safari Aventure : Des rencontres inoubliables</h1>
<p>Le Safari Aventure est la première étape incontournable. Vous montez dans votre voiture, et vous voilà en plein cœur de la savane! Lions, zèbres, et girafes viennent vous saluer de près. J’ai même dû tenir mon nez rouge bien serré quand une girafe a essayé de me faire un bisou avec sa grande langue! C’était tellement drôle que j’ai éclaté de rire, et je suis sûr que les girafes ont rigolé avec moi.</p>

<h1>Le Tunnel des Lions : Un spectacle impressionnant</h1>
<p>Ensuite, direction le Tunnel des Lions. Imaginez-vous entouré de lions majestueux qui se prélassent tout autour de vous. Moi, Giggles, j’ai essayé de leur faire mon meilleur rugissement, mais je crois que j’ai juste réussi à leur donner envie de bailler. Ces lions sont de véritables stars, et ils le savent bien!</p>

<h1>Promenade Safari : Un zoo à ciel ouvert</h1>
<p>Après cette rencontre rugissante, une petite promenade s’impose. La Promenade Safari est parfaite pour ça! Vous pouvez marcher parmi des animaux fascinants, comme des kangourous et des lémuriens. Moi, Giggles, j’ai tenté de faire des grimaces aux lémuriens, mais ils m’ont bien eu en me répondant avec leurs propres pitreries. On a bien rigolé ensemble!</p>

<h1>L'aire de jeux d'eau : Une pause rafraîchissante</h1>
<p>Après tant d’émotions, il était temps de se rafraîchir. Le Parc Safari propose une aire de jeux d'eau qui est parfaite pour cela! Des éclaboussures, des glissades et des rires à gogo, c’est tout ce qu’il fallait pour qu’un clown comme moi s’amuse. Les enfants et moi, on s'est lancés dans une bataille d'eau épique, et je crois bien qu’ils ont gagné!</p>

<h1>Un petit souvenir pour finir</h1>
<p>Avant de repartir, je ne pouvais pas manquer la boutique de souvenirs. Entre les peluches d'animaux, les t-shirts amusants et les chapeaux de safari, j’ai trouvé de quoi ramener un peu de cette journée mémorable chez moi. Et bien sûr, j’ai pris une petite peluche de lion pour me rappeler de cette aventure inoubliable.</p>

<h1>En conclusion : Une journée pleine de rires et de découvertes</h1>
<p>Le Parc Safari, c’est bien plus qu’une simple visite; c’est une aventure où chaque moment est rempli de surprises et de rires. Que vous soyez un amoureux des animaux ou un curieux en quête d'aventures, ce parc est un véritable trésor. Et avec Giggles, chaque instant devient encore plus amusant!</p>

<p>Alors, mettez votre chapeau de safari, venez rugir de plaisir avec moi, Giggles, et découvrez le Parc Safari comme vous ne l'avez jamais vu. Et souvenez-vous : là où il y a des rires et des animaux, Giggles est toujours prêt à s’amuser! 🎉🐾</p>

<p>À très bientôt pour une nouvelle journée pleine de giggles, mes amis!</p>`,
    clownIds: [1],
  },
  {
    title:
      "Une journée de rires et de frissons à La Ronde avec Chuckles le clown!",
    body: `<p>Salut les amis, c’est Chuckles, le clown toujours prêt pour une bonne dose de fun et d’aventures! Aujourd’hui, je vous emmène à La Ronde, le parc d’attractions où les sourires sont aussi hauts que les montagnes russes! Accrochez-vous bien, car cette journée va être un véritable tourbillon de rires et de frissons! 🎢🤡</p>

<h1>Une entrée en fanfare et en couleurs</h1>
<p>Dès que j’ai franchi les portes de La Ronde, j’ai su que j’étais au bon endroit. Des attractions à perte de vue, des enfants qui courent partout avec des yeux pleins d’étoiles, et moi, Chuckles, qui ne pouvait pas s’empêcher de sautiller partout! Mais avant de commencer, j’ai pris un petit selfie avec le grand carrousel… parce que, pourquoi pas?</p>

<h1>Les montagnes russes : Des frissons et des fous rires</h1>
<p>Si vous connaissez Chuckles, vous savez que j’adore les montagnes russes! Et à La Ronde, j’ai été servi! Le Goliath, c’est la star du parc, avec des descentes vertigineuses qui m’ont fait hurler de rire tout le long. Je crois bien que mon chapeau a fait trois tours sur lui-même avant de retomber sur ma tête!</p>

<p>Ensuite, direction le Monstre, une double montagne russe en bois qui fait vibrer de plaisir tous ceux qui osent y monter. J’ai pris place à l’avant pour être sûr de profiter à fond des secousses… et je n’ai pas été déçu! Chaque virage, chaque descente m’a fait éclater de rire, au point que j’en ai eu mal au ventre (mais dans le bon sens!).</p>

<h1>Les manèges pour toute la famille : Sourires garantis</h1>
<p>La Ronde, ce n’est pas que pour les amateurs de sensations fortes, c’est aussi un paradis pour les familles! Les petits manèges comme le Carrousel et le Tourbillon sont parfaits pour les enfants… et pour les clowns qui aiment s’amuser en douceur! Je me suis même laissé tenter par une petite balade dans le Grand Roue, qui offre une vue imprenable sur tout le parc. On se sent tout petit là-haut, mais quel spectacle!</p>

<h1>Le Village des petits : Le royaume des mini-clowns</h1>
<p>Les enfants ont leur propre royaume à La Ronde, et Chuckles ne pouvait pas rater ça! Le Pays de Ribambelle est un coin spécialement conçu pour les plus jeunes, avec des manèges colorés, des spectacles et des mascottes adorables. J’ai passé un moment à faire des grimaces avec les enfants, et on a bien rigolé ensemble!</p>

<h1>La Poutine et les délices du parc : Un régal pour les papilles</h1>
<p>Après toutes ces aventures, j’avais un petit creux. Et à La Ronde, on trouve de quoi régaler tout le monde! Je me suis arrêté pour une bonne poutine bien garnie, parce qu’après tout, on est au Québec! Entre les croustillants churros, les cornets de glace et les barbe-à-papa, j’ai trouvé de quoi satisfaire mon appétit de clown affamé.</p>

<h1>Les spectacles : Du fun en plein air</h1>
<p>La Ronde, c’est aussi des spectacles qui en mettent plein la vue! J’ai assisté à une représentation de danseurs acrobatiques, et je vous dis, ils étaient presque aussi souples que moi quand je fais mes acrobaties! C’était tellement divertissant que j’ai failli oublier de rire… mais heureusement, j’ai vite repris mes bonnes habitudes.</p>

<h1>En conclusion : Une journée inoubliable à La Ronde</h1>
<p>La Ronde, c’est bien plus qu’un simple parc d’attractions. C’est un endroit où chaque manège est une nouvelle aventure, où les sourires sont partout, et où même un clown comme moi peut se sentir chez lui. Que vous soyez un amateur de sensations fortes, un fan de manèges classiques ou simplement en quête de fun en famille, La Ronde a tout ce qu’il faut pour vous faire passer une journée mémorable.</p>

<p>Alors, préparez-vous à rire, à crier et à vous amuser avec moi, Chuckles, à La Ronde. Et souvenez-vous : là où il y a des montagnes russes et des sourires, Chuckles est toujours dans les parages! 🎉🎠</p>

<p>À très bientôt pour une nouvelle aventure pleine de rires et de frissons!</p>`,
    clownIds: [2],
  },
  {
    title: "Une journée de folie à La Ronde avec Giggles et Chuckles!",
    body: `<p>Giggles : Salut à tous, c’est Giggles, le clown avec un rire contagieux! 🎉 Aujourd’hui, je ne suis pas seul pour cette aventure incroyable à La Ronde! J’ai amené avec moi mon ami Chuckles, le roi des fous rires! Ensemble, on va explorer ce parc d’attractions de fond en comble, alors attachez vos ceintures… ou plutôt vos bretelles de clown!</p>

<p>Chuckles : Hé hé, salut tout le monde! Ici Chuckles, prêt à rire jusqu’à ce que mon chapeau tombe! 🤡 La Ronde, c’est le terrain de jeu idéal pour deux clowns comme nous, alors préparez-vous à une journée pleine de surprises, de loopings, et bien sûr, de rires à gogo!</p>

<h1>Les montagnes russes : Des rires et des sensations fortes!</h1>
<p>Giggles : On commence par les montagnes russes, et pas n’importe lesquelles! Le Goliath est un monstre de vitesse et de hauteur. On grimpe, on grimpe… et puis WOOSH! En bas à toute allure! Je riais tellement que j’en ai perdu mon chapeau. Heureusement, Chuckles l’a rattrapé… juste avant qu’il ne perde le sien! 🎢</p>

<p>Chuckles : Oh là là, le Vampire, c’était quelque chose! Les pieds dans le vide, la tête à l’envers, et Giggles qui hurlait à mes côtés… mais c’était surtout parce qu’il riait trop fort! Moi, j’essayais de garder mon nez rouge en place pendant tous ces loopings. Un vrai défi!</p>

<h1>Le carrousel : Une petite pause en douceur</h1>
<p>Giggles : Après tant d’émotions, une petite pause s’imposait. Direction le Carrousel pour une balade tranquille. Mais attention, on est des clowns après tout, alors on n’a pas pu s’empêcher de faire des grimaces à chaque tour! Les enfants autour de nous rigolaient tellement qu’on a failli en perdre l’équilibre… mais heureusement, Chuckles a des réflexes de clown!</p>

<p>Chuckles : Ah, le Carrousel… c’est vrai qu’on a bien rigolé! Et entre nous, je crois bien que Giggles a tenté de monter sur le cheval le plus petit… Résultat? Un grand éclat de rire quand il a essayé de tenir en équilibre!</p>

<h1>Les jeux d’adresse : Qui est le meilleur clown?</h1>
<p>Giggles : Ensuite, direction les stands de jeux d’adresse! Chuckles et moi avons décidé de voir qui était le meilleur au lancer de balles. Spoiler alert : on est tous les deux terribles! Mais qu’est-ce qu’on a rigolé! À la fin, c’est moi qui ai gagné un petit ourson en peluche, mais Chuckles a remporté… une tonne de fous rires!</p>

<p>Chuckles : Oui, bon, je dois l’admettre, Giggles a vraiment fait des miracles avec ces balles! Mais moi, j’ai découvert une nouvelle vocation : faire rire tout le monde en ratant mes tirs! Et franchement, c’est tout aussi amusant, non?</p>

<h1>La Grande Roue : Une vue imprenable et des éclats de rire</h1>
<p>Giggles : Avant de partir, on a décidé de monter dans la Grande Roue. Là-haut, on a une vue imprenable sur tout le parc… et bien sûr, sur les visages des gens qui s’amusent autant que nous. Chaque fois qu’on passait devant le photographe, on faisait des grimaces, et je suis sûr qu’il a capturé nos plus beaux éclats de rire!</p>

<p>Chuckles : C’est vrai que la vue était superbe… mais ce qui était encore mieux, c’était d’essayer de faire peur à Giggles en disant qu’on allait faire un looping avec la roue! (Bon, ça n’a pas marché, mais ça valait le coup d’essayer!)</p>

<h1>En conclusion : Une journée inoubliable à La Ronde</h1>
<p>Giggles : La Ronde, c’est l’endroit parfait pour s’amuser, se faire peur (juste un peu!), et surtout pour rire comme des fous. Entre les montagnes russes, les jeux, et les fous rires, on a passé une journée incroyable. Si vous cherchez à passer un bon moment, venez à La Ronde… et qui sait, peut-être qu’on se retrouvera dans une prochaine aventure!</p>

<p>Chuckles : Exactement, Giggles! La Ronde, c’est notre nouveau terrain de jeu préféré, et on ne peut pas attendre d’y retourner pour encore plus de fun et de rires. Alors, préparez-vous, parce que là où il y a Giggles et Chuckles, il y a toujours une bonne dose de folie!</p>

<p>Giggles & Chuckles : À bientôt pour une nouvelle journée pleine de rires et d’aventures, mes amis! 🎡🎉</p>`,
    clownIds: [1, 2],
  },
];

(async () => {
  await prisma.$transaction([
    prisma.clownsOnArticles.deleteMany(),
    prisma.clown.deleteMany(),
    prisma.article.deleteMany(),

    prisma.clown.createMany({
      data: CLOWNS.map((clown, clownId) => ({
        id: clownId,
        email: clown.email,
        name: clown.name,
        password: clown.password,
        isAdmin: clown.isAdmin,
      })),
    }),
    prisma.article.createMany({
      data: ARTICLES.map((article, articleId) => ({
        id: articleId,
        title: article.title,
        body: article.body,
      })),
    }),
    prisma.clownsOnArticles.createMany({
      data: ARTICLES.map((article, articleId) =>
        article.clownIds.map((clownId) => ({ clownId, articleId }))
      ).flat(),
    }),
  ]);
})();
