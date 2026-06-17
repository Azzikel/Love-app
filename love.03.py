import webbrowser
import os

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Our Love Story ❤️</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500&family=Dancing+Script:wght@500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#8B0000',
                        secondary: '#D4AF37',
                        light: '#FFF8F0',
                        crimson: '#DC143C',
                        rosegold: '#B76E79',
                        vintage: '#F5E6D3',
                        darkred: '#5C0000',
                        goldlight: '#F2E291',
                        blush: '#F8E2E7',
                        ivory: '#FFFFF0',
                        locked: '#94a3b8'
                    },
                    fontFamily: {
                        elegant: ['Playfair Display', 'serif'],
                        sans: ['Inter', 'sans-serif'],
                        script: ['Dancing Script', 'cursive']
                    },
                    boxShadow: {
                        'glow': '0 0 15px rgba(139, 0, 0, 0.3)',
                        'glow-gold': '0 0 15px rgba(212, 175, 55, 0.3)',
                       'soft': '0 8px 32px rgba(0,0,0,0.08)'
                    }
                }
            }
        }
    </script>
    <style>
        * {
            transition: all 0.5s ease;
        }
        body {
            transition: background 0.8s ease;
        }
        .fade-in {
            animation: fadeIn 1.2s ease-in;
        }
        .slide-up {
            animation: slideUp 1s ease-out;
        }
        .typing {
            border-right: 2px solid;
            white-space: pre-wrap;
            word-wrap: break-word;
            overflow-wrap: break-word;
            overflow: visible;
            max-width: 100%;
            animation: typing 3s steps(80, end), blink 0.75s step-end infinite;
        }
        .hover-lift {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .hover-lift:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.12);
        }
        .heart-float {
            position: absolute;
            color: #DC143C;
            font-size: 1.2rem;
            animation: float 6s linear infinite;
            opacity: 0;
        }
        .petal {
            position: absolute;
            width: 8px;
            height: 8px;
            background: #f8c8dc;
            border-radius: 50%;
            animation: fall 5s linear infinite;
            opacity: 0;
        }
        .glow-text {
            text-shadow: 0 0 8px currentColor;
        }
        .notification-alert {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: #DC143C;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            z-index: 9999;
            font-weight: 500;
            animation: alertPop 0.5s ease-out, fadeOut 0.5s ease-in 4s forwards;
        }
        .locked-btn {
            background-color: #e2e8f0 !important;
            color: #94a3b8 !important;
            cursor: not-allowed !important;
            transform: none !important;
            box-shadow: none !important;
        }
        .full-link {
            color: #8B0000;
            font-weight: 600;
            text-decoration: underline;
            margin-left: 8px;
            font-size: 0.75rem;
        }
        .full-link:hover {
            color: #DC143C;
        }
        .delete-btn {
            font-size: 0.65rem;
            padding: 2px 6px;
            background: #dc2626;
            color: white;
            border-radius: 4px;
            cursor: pointer;
            margin-left: 10px;
            border: none;
            font-weight: 600;
        }
        .delete-btn:hover {
            background: #b91c1c;
        }
        .clear-all-btn {
            font-size: 0.75rem;
            color: #dc2626;
            cursor: pointer;
            text-decoration: underline;
        }
        .clear-all-btn:hover {
            color: #991b1b;
        }
        .music-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 999;
            background: rgba(255,255,255,0.8);
            backdrop-blur: 4px;
            border: none;
            padding: 10px 14px;
            border-radius: 50%;
            font-size: 1.2rem;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .music-btn:hover {
            transform: scale(1.1);
            background: white;
        }
        @keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
        @keyframes slideUp { from {opacity:0; transform: translateY(20px);} to {opacity:1; transform: translateY(0);} }
        @keyframes typing { from {width:0;} to {width:100%;} }
        @keyframes blink { 50% {border-color:transparent;} }
        @keyframes float { 0% { transform:translateY(100vh) rotate(0deg); opacity:1; } 100% { transform:translateY(-100px) rotate(360deg); opacity:0; } }
        @keyframes fall { 0% { transform:translateY(-20px) rotate(0deg); opacity:0; } 100% { transform:translateY(100vh) rotate(360deg); opacity:0; } }
        @keyframes pulse { 0% { transform:scale(1); } 50% { transform:scale(1.05); } 100% { transform:scale(1); } }
        @keyframes alertPop { 0% { transform:translateX(-50%) translateY(-20px); opacity:0; } 100% { transform:translateX(-50%) translateY(0); opacity:1; } }
        @keyframes fadeOut { to { opacity:0; visibility:hidden; } }
        .animate-pulse-slow { animation: pulse 3s infinite; }
        .theme-elegant { background: #F5E6D3; color: #2b2b2b; }
        .theme-rosegold { background: linear-gradient(135deg, #F8E2E7, #B76E7940); color: #4a2c2a; }
        .theme-crimson { background: linear-gradient(135deg, #5C0000, #DC143C30); color: #fff; }
        .theme-simple { background: #FFF8F0; color: #333; }
    </style>
</head>
<body class="font-sans bg-vintage min-h-screen relative overflow-x-hidden theme-elegant">
    <!-- Background Animation -->
    <div id="bg" class="fixed inset-0 -z-10 pointer-events-none"></div>
    <div id="heartsContainer" class="fixed inset-0 -z-5 pointer-events-none"></div>

    <!-- Access Mode with Password -->
    <div class="fixed top-4 right-4 z-50 bg-white/80 backdrop-blur-sm p-2 rounded-lg shadow-soft hover:shadow-glow">
        <select id="mode" class="border-none bg-transparent font-medium">
            <option value="viewer">Viewer Mode</option>
            <option value="owner">Owner Mode</option>
        </select>
        <div id="passwordBox" class="hidden mt-2">
            <input type="password" id="ownerPass" placeholder="Enter Password" class="px-2 py-1 border rounded w-28 focus:ring-2 focus:ring-secondary/50">
            <button id="unlockBtn" class="ml-1 px-2 py-1 bg-secondary text-white rounded hover:bg-secondary/90 hover-lift">Go</button>
        </div>
    </div>

    <div class="container mx-auto px-4 py-8 max-w-6xl">
        <!-- MVP: Dashboard -->
        <section class="text-center fade-in mb-20">
            <h1 class="font-elegant text-[clamp(2.5rem,6vw,4rem)] font-bold text-primary mb-6 glow-text">Our Love Story</h1>
            <div class="bg-white/70 backdrop-blur-sm rounded-3xl shadow-soft p-10 mb-10 hover:shadow-glow transition-all">
                <h2 class="text-gray-700 text-xl mb-3">Days Together Since September 24, 2024</h2>
                <div id="daysCounter" class="text-6xl font-elegant font-bold text-secondary mt-2 animate-pulse-slow"></div>
            </div>
            <div class="grid md:grid-cols-2 gap-8 mb-10">
                <div class="bg-white/70 backdrop-blur-sm p-8 rounded-2xl shadow-soft hover:shadow-glow">
                    <h3 class="text-gray-700 text-lg mb-2">Next Monthsary (Every 24th)</h3>
                    <div id="monthsaryCountdown" class="text-3xl font-semibold text-primary"></div>
                </div>
                <div class="bg-white/70 backdrop-blur-sm p-8 rounded-2xl shadow-soft hover:shadow-glow">
                    <h3 class="text-gray-700 text-lg mb-2">Next Anniversary (Sept 24)</h3>
                    <div id="anniversaryCountdown" class="text-3xl font-semibold text-crimson"></div>
                </div>
            </div>
            <!-- Theme Switcher -->
            <div class="flex justify-center gap-4 flex-wrap mb-12">
                <button class="theme-btn px-6 py-3 rounded-full shadow-soft font-medium hover-lift active:scale-95" data-theme="elegant">Elegant / Vintage</button>
                <button class="theme-btn px-6 py-3 rounded-full shadow-soft font-medium hover-lift active:scale-95" data-theme="rosegold">Luxury Rose Gold</button>
                <button class="theme-btn px-6 py-3 rounded-full shadow-soft font-medium hover-lift active:scale-95" data-theme="crimson">Royal Crimson</button>
                <button class="theme-btn px-6 py-3 rounded-full shadow-soft font-medium hover-lift active:scale-95" data-theme="simple">Soft & Simple</button>
            </div>
        </section>

        <!-- Letters Section -->
        <section class="mb-20 slide-up">
            <h2 class="font-elegant text-4xl text-primary text-center mb-8 glow-text">Letters for You</h2>
            <div class="grid sm:grid-cols-3 gap-5">
                <button class="letter-btn bg-white/60 backdrop-blur-sm p-5 rounded-xl shadow-soft hover:shadow-glow font-medium hover-lift" data-type="daily">
                    Daily Letter
                    <p class="text-xs text-gray-500 mt-1">Available: Every Day</p>
                </button>
                <button class="letter-btn bg-white/60 backdrop-blur-sm p-5 rounded-xl shadow-soft hover:shadow-glow font-medium hover-lift" data-type="random">
                    Random Letter
                    <p class="text-xs text-gray-500 mt-1">Available: Every Day</p>
                </button>
                <button class="letter-btn bg-white/60 backdrop-blur-sm p-5 rounded-xl shadow-soft hover:shadow-glow font-medium hover-lift locked-btn" data-type="monthsary" data-lock="true">
                    🔒 Monthsary Letter
                    <p class="text-xs text-gray-500 mt-1">Available: Every 24th of the month</p>
                </button>
                <button class="letter-btn bg-white/60 backdrop-blur-sm p-5 rounded-xl shadow-soft hover:shadow-glow font-medium hover-lift locked-btn" data-type="anniversary" data-lock="true">
                    🔒 Anniversary Letter
                    <p class="text-xs text-gray-500 mt-1">Available: Every September 24</p>
                </button>
                <button class="letter-btn bg-white/60 backdrop-blur-sm p-5 rounded-xl shadow-soft hover:shadow-glow font-medium hover-lift locked-btn" data-type="valentine" data-lock="true">
                    🔒 Valentine Letter
                    <p class="text-xs text-gray-500 mt-1">Available: Every February 14</p>
                </button>
                <button class="letter-btn bg-white/60 backdrop-blur-sm p-5 rounded-xl shadow-soft hover:shadow-glow font-medium hover-lift" data-type="missme">
                    Open When You Miss Me
                    <p class="text-xs text-gray-500 mt-1">Available: Any time</p>
                </button>
                <button class="letter-btn bg-white/60 backdrop-blur-sm p-5 rounded-xl shadow-soft hover:shadow-glow font-medium hover-lift" data-type="sad">
                    Open When You’re Sad
                    <p class="text-xs text-gray-500 mt-1">Available: Any time</p>
                </button>
                <button class="letter-btn bg-white/60 backdrop-blur-sm p-5 rounded-xl shadow-soft hover:shadow-glow font-medium hover-lift" data-type="needlove">
                    Open When You Need Love
                    <p class="text-xs text-gray-500 mt-1">Available: Any time</p>
                </button>
                <button class="letter-btn bg-white/60 backdrop-blur-sm p-5 rounded-xl shadow-soft hover:shadow-glow font-medium hover-lift" data-type="proud">
                    Open When You’re Proud Of Us
                    <p class="text-xs text-gray-500 mt-1">Available: Any time</p>
                </button>
            </div>
            <div id="letterDisplay" class="mt-10 bg-white/80 backdrop-blur-sm rounded-2xl p-8 min-h-[200px] w-full whitespace-pre-wrap break-words shadow-soft text-lg leading-relaxed"></div>
        </section>

        <!-- Poem Section -->
        <section class="mb-20 fade-in text-center">
            <h2 class="font-elegant text-4xl text-secondary mb-8 glow-text">Love Poems for You</h2>
            <button id="getPoem" class="bg-secondary/90 text-white px-8 py-4 rounded-full shadow-glow-gold hover:bg-secondary hover-lift font-medium text-lg">Show New Poem</button>
            <div id="poemDisplay" class="mt-8 text-xl font-elegant whitespace-pre-line min-h-[150px] bg-white/60 backdrop-blur-sm p-8 rounded-2xl shadow-soft leading-relaxed"></div>
        </section>

        <!-- Surprise Section -->
        <section class="mb-20 text-center slide-up">
            <h2 class="font-elegant text-3xl text-primary mb-6">Little Surprises for You</h2>
            <button id="surpriseBtn" class="bg-primary/10 text-primary px-6 py-3 rounded-full shadow-soft hover:bg-primary/20 hover-lift font-medium">Reveal Today’s Compliment</button>
            <p id="surpriseText" class="mt-6 text-xl italic font-script text-primary/80"></p>
        </section>

        <!-- Daily Connection -->
        <section class="mb-20 fade-in">
            <h2 class="font-elegant text-3xl text-secondary text-center mb-6">Daily Connection</h2>
            <div class="bg-white/70 backdrop-blur-sm rounded-2xl p-8 shadow-soft">
                <p class="mb-4 text-lg">How are you feeling about us today, my love, Caroline?</p>
                <textarea id="feelingInput" class="w-full p-4 border rounded-xl mb-5 focus:ring-2 focus:ring-secondary/50 min-h-[100px]" placeholder="Share your thoughts, feelings, or sweet memories..."></textarea>
                <p class="mb-3 font-medium">Mood:</p>
                <div class="flex gap-4 flex-wrap mb-6">
                    <span class="mood-btn px-5 py-2 rounded-full bg-green-100 hover:bg-green-200 cursor-pointer transition-all" data-mood="happy">Happy 💛</span>
                    <span class="mood-btn px-5 py-2 rounded-full bg-blue-100 hover:bg-blue-200 cursor-pointer transition-all" data-mood="sad">Soft / Quiet 💙</span>
                    <span class="mood-btn px-5 py-2 rounded-full bg-purple-100 hover:bg-purple-200 cursor-pointer transition-all" data-mood="missing">Missing You 💜</span>
                    <span class="mood-btn px-5 py-2 rounded-full bg-yellow-100 hover:bg-yellow-200 cursor-pointer transition-all" data-mood="excited">Excited 💖</span>
                </div>
                <button id="saveBtn" class="bg-secondary text-white px-6 py-3 rounded-xl shadow-soft hover:bg-secondary/90 hover-lift font-medium">Save This Moment</button>
            </div>
        </section>

        <!-- OWNER PANEL - FULL WITH ALL BUTTONS -->
        <section id="ownerPanel" class="hidden mb-20 fade-in border-2 border-secondary/50 rounded-2xl p-8 bg-white/60 backdrop-blur-sm shadow-soft">
            <h2 class="font-elegant text-3xl text-secondary text-center mb-6">📖 Owner Log - Everything Recorded</h2>
            <div class="mb-8">
                <h3 class="font-semibold text-lg mb-2 flex justify-between items-center">
                    💌 Letters Opened:
                    <span class="clear-all-btn" id="clearAllLetters">Clear All</span>
                </h3>
                <ul id="logLetters" class="list-disc pl-6 text-sm space-y-1 max-h-40 overflow-y-auto"></ul>
            </div>
            <div class="mb-8">
                <h3 class="font-semibold text-lg mb-2 flex justify-between items-center">
                    📜 Poems Shown:
                    <span class="clear-all-btn" id="clearAllPoems">Clear All</span>
                </h3>
                <ul id="logPoems" class="list-disc pl-6 text-sm space-y-1 max-h-40 overflow-y-auto"></ul>
            </div>
            <div class="mb-8">
                <h3 class="font-semibold text-lg mb-2 flex justify-between items-center">
                    ✨ Surprises / Compliments:
                    <span class="clear-all-btn" id="clearAllSurprises">Clear All</span>
                </h3>
                <ul id="logSurprises" class="list-disc pl-6 text-sm space-y-1 max-h-40 overflow-y-auto"></ul>
            </div>
            <div>
                <h3 class="font-semibold text-lg mb-2 flex justify-between items-center">
                    📝 Her Feelings, Mood & Thoughts:
                    <span class="clear-all-btn" id="clearAllReflections">Clear All</span>
                </h3>
                <ul id="logReflections" class="list-disc pl-6 text-sm space-y-2 max-h-60 overflow-y-auto"></ul>
            </div>
        </section>
    </div>

    <!-- Full Letter Modal -->
    <div id="fullLetterModal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-[9999] hidden items-center justify-center p-4">
        <div class="bg-white rounded-2xl p-8 max-w-2xl w-full max-h-[80vh] overflow-y-auto shadow-glow">
            <h3 class="font-elegant text-2xl text-primary mb-4" id="modalTitle"></h3>
            <div id="modalContent" class="text-lg leading-relaxed whitespace-pre-wrap"></div>
            <button onclick="closeModal()" class="mt-6 bg-primary text-white px-6 py-2 rounded-lg hover:bg-primary/90">Close</button>
        </div>
    </div>

    <script>
        const START_DATE = new Date(2024, 8, 24);
        const OWNER_PASSWORD = "924";

        let logs = {
            letters: JSON.parse(localStorage.getItem("log_letters")) || [],
            poems: JSON.parse(localStorage.getItem("log_poems")) || [],
            surprises: JSON.parse(localStorage.getItem("log_surprises")) || [],
            reflections: JSON.parse(localStorage.getItem("log_reflections")) || []
        };
        let openedLetters = JSON.parse(localStorage.getItem("openedLetters")) || { monthsary: {}, anniversary: {}, valentine: {} };

        function sendNotification(title, message) {
            const alertBox = document.createElement('div');
            alertBox.className = 'notification-alert';
            alertBox.innerHTML = `<b>${title}</b><br>${message}`;
            document.body.appendChild(alertBox);
            setTimeout(() => alertBox.remove(), 4500);
            if (Notification.permission === "granted") new Notification(title, { body: message });
        }
        if (Notification.permission !== "granted") Notification.requestPermission();

        function checkLetterLocks() {
            const today = new Date();
            const day = today.getDate(), month = today.getMonth() + 1, year = today.getFullYear();
            document.querySelectorAll('.letter-btn[data-lock="true"]').forEach(btn => {
                const type = btn.dataset.type;
                let unlocked = false;
                if (type === 'monthsary' && day === 24) unlocked = true;
                if (type === 'anniversary' && month === 9 && day === 24) unlocked = true;
                if (type === 'valentine' && month === 2 && day === 14) unlocked = true;

                if (!unlocked) {
                    btn.classList.add('locked-btn'); btn.disabled = true;
                } else {
                    const key = `${type}_${year}_${month}_${day}`;
                    if (!openedLetters[type][key]) {
                        sendNotification("💌 Special Letter Ready!", `Your ${type} letter is here`);
                        openedLetters[type][key] = true;
                        localStorage.setItem("openedLetters", JSON.stringify(openedLetters));
                    }
                    btn.classList.remove('locked-btn'); btn.disabled = false;
                    btn.innerHTML = btn.innerHTML.replace('🔒', '✨');
                }
            });
        }

        const LETTERS_DB = {
            daily: [
`Every morning when I wake up, you are the first thing I think of, my love, Caroline. You make my whole day happy just by being in it. Even on hard days, just knowing you are mine makes me smile.

You don’t have to do anything special to make me happy. Just being you is enough. No matter what happens today, remember I am always here for you. I love you more today than yesterday, but not as much as tomorrow.

You are my favorite part of every day, my love, Caroline. Thank you for being mine.`,
`Every day I find new reasons to love you, my love, Caroline. I love how you laugh, how kind you are, and how you look at me like I am the best thing in your life. You make simple moments feel like magic.

Life changes a lot, but one thing will never change: my love for you. It grows bigger and deeper every day. I promise I will always stay by your side, through good times and bad.

You are not just my partner — you are my best friend and my home. Thank you for loving me, my love, Caroline.`,
`My day starts and ends with you in my heart, my love, Caroline. From the moment I open my eyes until I sleep, you are always on my mind. You make me feel safe, happy, and loved.

Sometimes I wonder how I got so lucky. I get to love you, hold you, and call you mine. Everything you do, big or small, means so much to me. You make me want to be better, just because you deserve the best.

Please remember: you are loved so much, more than I can say. You are my everything, my love, Caroline.`
            ],
            random: [
`Love is not just about big days or fancy things. Love is in the small moments — when we laugh together, when we talk, or when you hold my hand. It is how you understand me without me saying a word.

You taught me what love really means. Love is kind, patient, and never ends. With you, my love, Caroline, I learned that love is a choice I make every day. And I will always choose you.

You are my best memory and my best future. I love you so much, my love, Caroline.`,
`You are the best thing that ever happened to me, my love, Caroline. Before I met you, I did not know how happy life could be. You brought so much light and love into my world.

We don’t need perfect days. We just need each other. Even when things are hard, being together makes it okay. You make good times better and hard times easier.

I am so proud of what we have. You are my heart and my forever, my love, Caroline.`,
`My heart knows you, my love, Caroline. It beats only for you. The first time I saw you, I knew you were the one I was waiting for. Now I have you, and I never want to let go.

You are my safe place. No matter where I go, I always come back to you. You understand me like no one else. You love me in the best way.

Thank you for staying with me. I love you more than the stars, my love, Caroline.`
            ],
            monthsary: [
`Happy monthsary, my love, Caroline! Every month feels like a beautiful new page in our story. It feels like just yesterday we started, but also like I have known you forever.

Every month we spend together, I love you more. We learn together, we grow together, and we love deeper. You taught me how to be patient, kind, and how to care for someone so much.

Thank you for being my partner and my best friend. Here is to many more months and years together. I love you always, my love, Caroline.`,
`Another month has passed, and we have so many sweet memories now. Time flies so fast when I am with you, my love, Caroline. Every day feels like a celebration because of you.

I look back and see how far we have come. We built something strong and real. You are the sweetest and most loving partner.

Every month makes me see how lucky I am. You make life beautiful. Happy monthsary, my love, Caroline — I love us.`,
`Happy monthsary, my love, Caroline! Every time this day comes, I remember how lucky I am. You make my world bright just by being there.

This month had happy days and quiet days, but through it all, my love for you only grew. You always make me feel loved and cared for.

I promise to keep loving you, every single day. You are my forever, my love, Caroline.`
            ],
            anniversary: [
`Happy anniversary, my love, Caroline! Looking back at all the time we have been together, I know how lucky I am. You are my home, my best friend, and my greatest love.

We went through happy days and hard days. Through all of it, you stayed by my side. You showed me what true love is — loyal and never ending.

I would choose you again and again, every time. You are the love I want forever. Thank you for making my life so beautiful. I love you, my love, Caroline.`,
`Every year with you is better than the last, my love, Caroline. We grew, we learned, we laughed, and we loved so much. I am so proud of what we have built.

You know me best and love me most. Life without you would be empty and dark. You bring light and joy to everything.

Anniversary means another year of love. But to me, it means another year of having you — the best gift ever. Many more years to come, my love, Caroline.`,
`From the first day until now, my love for you only got stronger. You are such a big part of me now, I cannot imagine life without you, my love, Caroline.

Every year with you is a gift. You make me feel loved and special. You taught me so much about life and love.

Today I celebrate us and our love. You are my forever and always. Happy anniversary, my love, Caroline.`
            ],
            valentine: [
`To my forever valentine, my love, Caroline: You make every day feel like Valentine’s Day. You don’t need a special date to be special to me — you are special every day.

You are the kindest and sweetest person I know. You make everyone happy, but you make me the happiest of all.

I give you all my heart, all my love, and all of me. Everything I have is yours. I love you forever, my love, Caroline.`,
`Every day I love you more than the day before, my love, Caroline. You are my heart and my true love. Valentine’s Day is just one day, but my love for you is every day, every minute.

You bring so much joy into my life. You make me feel so loved. You understand me and support me always.

I promise to keep making you happy every day. You are my forever valentine, my love, Caroline.`,
`Life without you would be like a day without sun, or a sky without stars. You are what makes my life full and happy, my love, Caroline.

You are my favorite person to be with and to talk to. Every moment with you is precious.

I love you more than anything sweet or beautiful. You are my one true love. Happy Valentine’s Day, my love, Caroline.`
            ],
            missme: [
`Open this when you miss me, my love, Caroline. Remember: I am always with you, even when we are apart. Close your eyes and feel my love around you.

Distance is only for a short time, but what we have is forever. No matter how far apart, our hearts are together. I think of you every second, and I miss you too.

When you feel lonely, remember I am thinking of you and smiling because of you. We are never really apart, because you are always in my heart.

I love you, I miss you, and I wait for the day I can hold you again, my love, Caroline.`,
`Whenever you miss me, my love, Caroline, know I miss you just as much. Distance only tests how strong our love is — and ours is very strong.

Even far away, you are the first thing I think of when I wake up and last before I sleep. You are with me everywhere I go.

Don’t feel sad. I am right here in your heart. Nothing can separate us.

I love you deeply. I will be with you soon, my love, Caroline.`,
`Missing you is just my heart saying how much I love you, my love, Caroline. Every time I miss you, I know more and more that you are my whole world.

No matter where we are, our love connects us. You are never alone, because I am walking with you in my heart.

Keep me in your heart, just like I keep you in mine. We will be together soon. You are loved so much, my love, Caroline.`
            ],
            sad: [
`Open this when you are sad or tired, my love, Caroline. Remember: I am your safe place. You can cry, you can be quiet, you can feel anything — I am here to hold you.

You don’t have to carry everything alone. I will share all your worries. I will remind you how strong and wonderful you are. Even when you forget, I will not.

Hard days pass, but my love stays. I am your light and your comfort. We will get through this together.

You are loved so much, and never alone, my love, Caroline.`,
`When things feel heavy, lean on me, my love, Caroline. I will carry you, I will listen, and I will love you through it all. It is okay to feel sad — you are still loved.

Your happiness means everything to me. I will do anything to make you smile again.

Sadness is just a cloud that goes away. The sun will shine again. I will be right here with you, holding your hand.

You are precious and strong, my love, Caroline.`,
`Your feelings matter so much to me, my love, Caroline. Never think you are a burden. You can be soft, you can be weak, you can be yourself — and I love you even more for it.

I am here to listen, to understand, and to stay. Whatever you go through, we face it together. You are not fighting alone.

Even in hard times, remember: you are loved, you are important, and you are never forgotten. I am always here, my love, Caroline.`
            ],
            needlove: [
`Open this when you need love, my love, Caroline. My love for you never ends, never fades, never changes. It only grows bigger every day.

You are loved for who you are. Loved when you are happy, loved when you are sad, loved always.

My love is bigger than the sky, deeper than the sea. It is all yours, forever.

Never doubt it. You are the most loved person in my life, my love, Caroline.`,
`You are loved, cherished, and so special to me, my love, Caroline. You are the best gift I ever got.

When you feel unsure, remember: I love you more than anything. I love you with all my heart.

You don’t have to do anything to earn my love. You don’t have to be perfect. I love you just because you are you — and that is enough.

My promise: I will love you always, my love, Caroline.`,
`Love is not just a feeling. It is a promise I made to you, my love, Caroline. I promise to love you, care for you, respect you, and stay with you always.

You are the reason I wake up happy. You make my life full of love and meaning.

Remember: you are never alone, never unloved. I am always here, loving you.

You are my everything, my love, Caroline.`
            ],
            proud: [
`Open this when you are proud of us, my love, Caroline. We are my favorite story, my best dream come true.

Look at what we built. We have a love that is real and strong. We have a life many people wish for.

I am proud of you, proud of me, proud of us. I am proud how we love each other and help each other grow. We are not perfect, but we are real — and that is perfect for me.

I love what we are. We are amazing, my love, Caroline.`,
`Look how far we came! We started as strangers, now we are one heart, one life, my love, Caroline. We went through so much, learned so much, loved so much.

We built something nothing can break. We learned to trust, to forgive, to love without limits.

I am proud of every memory, every step. I love how you love me, and how I love you. We fit perfectly together.

You make me proud every day. Together we are the best, my love, Caroline.`,
`We don’t have everything, but we have each other — and that is everything, my love, Caroline. We have love, trust, and friendship.

I am proud of our love, our life, and our future. I am proud how we handle hard times and how we enjoy good times.

You make me proud just by being the kind and wonderful person you are. Being with you makes me the happiest and proudest person.

I love us, I love you, my love, Caroline.`
            ]
        };

        const POEMS_DB = [
`Your smile is my sun, warm and bright,
Your voice feels like sweet music in the night.
With every beat of my heart, every breath I take,
I love you more than words can make.

You keep me calm when things go wrong,
You are my safe place, where I belong.
No matter where life takes me to,
I will always love only you — my love, Caroline.`,

`Like stars that shine in dark night sky,
Your love makes my whole world bright.
Through happy days and days of pain,
My heart will always say your name.

You are the dream I always knew,
The only one I want to be true.
With you, forever feels so near,
Every moment with you is dear — my love, Caroline.`,

`You are the sweetest thought I have,
The dream I see when morning comes.
Every word I say, every part of me,
Is filled with love only for thee.

You are the song I always sing,
You are the one who makes my heart ring.
My love for you will never die,
It stays with me until I die — my love, Caroline.`,

`Hand in hand we walk this way,
Our love grows stronger every day.
No distance far, no time too long,
My heart stays right where you belong.

Through every high and every low,
Together is the way we go.
You are my life, my hope, my all,
My greatest love, my endless call — my love, Caroline.`
        ];

        const COMPLIMENTS_DB = [
            "You have the kindest heart I ever saw, full of love and warmth, my love, Caroline.",
            "Every day with you is the best day, because you make everything nice, my love, Caroline.",
            "I love how you see the world — bright and full of love, just like you, my love, Caroline.",
            "You are my biggest blessing and my sweetest dream, my love, Caroline.",
            "Your smile makes everyone happy, and it makes my day perfect, my love, Caroline.",
            "You are strong, smart, gentle, and wonderful — I love everything about you, my love, Caroline.",
            "When you look at me, I feel like the most special person alive, my love, Caroline.",
            "You are the best partner and best friend. I am so lucky you are mine, my love, Caroline.",
            "You make me better every day. You help me and love me so well, my love, Caroline.",
            "You are beautiful inside and out. Every day I love you more, my love, Caroline."
        ];

        function getRandom(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
        function nowTime() { return new Date().toLocaleString(); }

        function openFullLetter(title, content) {
            document.getElementById('modalTitle').textContent = title;
            document.getElementById('modalContent').textContent = content;
            document.getElementById('fullLetterModal').style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }
        function closeModal() {
            document.getElementById('fullLetterModal').style.display = 'none';
            document.body.style.overflow = 'auto';
        }

        function updateCounters() {
            const today = new Date();
            const diffDays = Math.floor((today - START_DATE) / (1000 * 60 * 60 * 24));
            document.getElementById('daysCounter').textContent = diffDays;

            let nextMonthsary = new Date(today.getFullYear(), today.getMonth(), 24);
            if (today.getDate() > 24) nextMonthsary.setMonth(nextMonthsary.getMonth() + 1);
            updateCountdown(nextMonthsary, 'monthsaryCountdown');

            let nextAnniversary = new Date(today.getFullYear(), 8, 24);
            if (today > nextAnniversary) nextAnniversary.setFullYear(nextAnniversary.getFullYear() + 1);
            updateCountdown(nextAnniversary, 'anniversaryCountdown');
        }

        function updateCountdown(targetDate, elementId) {
            const now = new Date();
            const diff = targetDate - now;
            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            document.getElementById(elementId).textContent = `${days}d ${hours}h ${mins}m`;
        }

        function createHeartBurst() {
            const container = document.getElementById('heartsContainer');
            for (let i = 0; i < 15; i++) {
                const heart = document.createElement('div');
                heart.className = 'heart-float';
                heart.textContent = '❤️';
                heart.style.left = `${Math.random() * 100}%`;
                heart.style.animationDelay = `${Math.random() * 4}s`;
                container.appendChild(heart);
                setTimeout(() => heart.remove(), 6000);
            }
        }

        function updateOwnerPanel() {
            const letterList = document.getElementById("logLetters");
            letterList.innerHTML = "";
            logs.letters.forEach((item, index) => {
                const li = document.createElement("li");
                li.innerHTML = `${item.time} — ${item.type} 
                    <a href="javascript:void(0)" onclick="openFullLetter('${item.type} Letter', \`${item.fullContent}\`)" class="full-link">View Full Letter</a> 
                    <button class="delete-btn" data-type="letters" data-index="${index}">×</button>`;
                letterList.appendChild(li);
            });

            const poemList = document.getElementById("logPoems");
            poemList.innerHTML = "";
            logs.poems.forEach((item, index) => {
                const li = document.createElement("li");
                li.innerHTML = `${item.time} 
                    <a href="javascript:void(0)" onclick="openFullLetter('Love Poem', \`${item.fullContent}\`)" class="full-link">View Full Poem</a> 
                    <button class="delete-btn" data-type="poems" data-index="${index}">×</button>`;
                poemList.appendChild(li);
            });

            const surpriseList = document.getElementById("logSurprises");
            surpriseList.innerHTML = "";
            logs.surprises.forEach((item, index) => {
                const li = document.createElement("li");
                li.innerHTML = `${item.time} — ${item.content} 
                    <button class="delete-btn" data-type="surprises" data-index="${index}">×</button>`;
                surpriseList.appendChild(li);
            });

            const reflList = document.getElementById("logReflections");
            reflList.innerHTML = "";
            logs.reflections.forEach((item, index) => {
                const li = document.createElement("li");
                li.innerHTML = `${item.time} [${item.mood}] — ${item.text} 
                    <button class="delete-btn" data-type="reflections" data-index="${index}">×</button>`;
                reflList.appendChild(li);
            });

            document.querySelectorAll(".delete-btn").forEach(btn => {
                btn.addEventListener("click", () => {
                    const type = btn.dataset.type;
                    const idx = parseInt(btn.dataset.index);
                    logs[type].splice(idx, 1);
                    localStorage.setItem(`log_${type}`, JSON.stringify(logs[type]));
                    updateOwnerPanel();
                });
            });
        }

        document.getElementById("clearAllLetters").addEventListener("click", () => {
            if (confirm("Delete ALL letter history?")) { logs.letters = []; localStorage.setItem("log_letters", JSON.stringify(logs.letters)); updateOwnerPanel(); }
        });
        document.getElementById("clearAllPoems").addEventListener("click", () => {
            if (confirm("Delete ALL poem history?")) { logs.poems = []; localStorage.setItem("log_poems", JSON.stringify(logs.poems)); updateOwnerPanel(); }
        });
        document.getElementById("clearAllSurprises").addEventListener("click", () => {
            if (confirm("Delete ALL surprise history?")) { logs.surprises = []; localStorage.setItem("log_surprises", JSON.stringify(logs.surprises)); updateOwnerPanel(); }
        });
        document.getElementById("clearAllReflections").addEventListener("click", () => {
            if (confirm("Delete ALL feelings history?")) { logs.reflections = []; localStorage.setItem("log_reflections", JSON.stringify(logs.reflections)); updateOwnerPanel(); }
        });

        document.querySelectorAll('.letter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                if (btn.disabled) return;
                const text = getRandom(LETTERS_DB[btn.dataset.type]);
                const display = document.getElementById('letterDisplay');
                display.innerHTML = `<p class="typing">${text}</p>`;
                createHeartBurst();
                logs.letters.unshift({ time: nowTime(), type: btn.dataset.type, content: text.substring(0,60)+'...', fullContent: text });
                localStorage.setItem("log_letters", JSON.stringify(logs.letters));
                updateOwnerPanel();
            });
        });

        document.getElementById('getPoem').addEventListener('click', () => {
            const poem = getRandom(POEMS_DB);
            document.getElementById('poemDisplay').textContent = poem;
            createHeartBurst();
            logs.poems.unshift({ time: nowTime(), fullContent: poem });
            localStorage.setItem("log_poems", JSON.stringify(logs.poems));
            updateOwnerPanel();
        });

        document.getElementById('surpriseBtn').addEventListener('click', () => {
            const surprise = getRandom(COMPLIMENTS_DB);
            document.getElementById('surpriseText').textContent = surprise;
            createHeartBurst();
            sendNotification("Sweet Message 💌", surprise);
            logs.surprises.unshift({ time: nowTime(), content: surprise });
            localStorage.setItem("log_surprises", JSON.stringify(logs.surprises));
            updateOwnerPanel();
        });

        let selectedMood = "";
        document.querySelectorAll('.mood-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.mood-btn').forEach(b => b.classList.remove('bg-pink-200','font-bold'));
                btn.classList.add('bg-pink-200','font-bold');
                selectedMood = btn.dataset.mood;
            });
        });

        document.getElementById('saveBtn').addEventListener('click', () => {
            const text = document.getElementById('feelingInput').value.trim();
            if (!text || !selectedMood) { alert("Please write something and pick a mood first!"); return; }
            sendNotification("Saved ✅", "Your thought and mood are kept safe with love.");
            document.getElementById('feelingInput').value = "";
            document.querySelectorAll('.mood-btn').forEach(b => b.classList.remove('bg-pink-200','font-bold'));
            logs.reflections.unshift({ time: nowTime(), mood: selectedMood, text: text });
            localStorage.setItem("log_reflections", JSON.stringify(logs.reflections));
            updateOwnerPanel();
            selectedMood = "";
        });

        const modeSelect = document.getElementById('mode');
        const passwordBox = document.getElementById('passwordBox');
        const ownerPanel = document.getElementById('ownerPanel');
        const ownerPass = document.getElementById('ownerPass');
        const unlockBtn = document.getElementById('unlockBtn');

        modeSelect.addEventListener('change', () => {
            if (modeSelect.value === 'owner') { passwordBox.classList.remove('hidden'); ownerPass.value = ""; }
            else { passwordBox.classList.add('hidden'); ownerPanel.classList.add('hidden'); }
        });

        unlockBtn.addEventListener('click', () => {
            if (ownerPass.value === OWNER_PASSWORD) {
                ownerPanel.classList.remove('hidden');
                passwordBox.classList.add('hidden');
                sendNotification("✅ Unlocked", "Welcome back, my love. All memories are here.");
                updateOwnerPanel();
            } else { alert("Wrong password, my love. Try again."); }
        });

        document.querySelectorAll('.theme-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.body.className = document.body.className.replace(/theme-\w+/g, '');
                document.body.classList.add(`theme-${btn.dataset.theme}`);
                sendNotification("🎨 Theme Changed", "Our story looks beautiful in this style too.");
            });
        });

        updateCounters();
        setInterval(updateCounters, 60000);
        checkLetterLocks();
        setInterval(checkLetterLocks, 3600000);

        setInterval(() => {
            const petal = document.createElement('div');
            petal.className = 'petal';
            petal.style.left = `${Math.random() * 100}%`;
            petal.style.animationDelay = `${Math.random() * 5}s`;
            document.getElementById('heartsContainer').appendChild(petal);
            setTimeout(() => petal.remove(), 5000);
        }, 300);
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    file_path = "our_love_story.html"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    webbrowser.open('file://' + os.path.abspath(file_path))
    print(f"✨ Love story opened at: {file_path}")