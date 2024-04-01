<script lang="ts">
    import { useLazyImage as lazyImage } from 'svelte-lazy-image';
    import {generate_cards} from './cards.ts';
    import {get_index_of_card} from './cards.ts';
    import ball from '$lib/images/magic.gif'
    import cloud2 from '$lib/images/cloud2.png'
    import c0 from '$lib/images/0.jpg'
    import c1 from '$lib/images/1.jpg'
    import c2 from '$lib/images/2.jpg'
    import c3 from '$lib/images/3.jpg'
    import c4 from '$lib/images/4.jpg'
    import c5 from '$lib/images/5.jpg'
    import c6 from '$lib/images/6.jpg'
    import c7 from '$lib/images/7.jpg'
    import c8 from '$lib/images/8.jpg'
    import c9 from '$lib/images/9.jpg'
    import c10 from '$lib/images/10.jpg'
    import c11 from '$lib/images/11.jpg'
    import c12 from '$lib/images/12.jpg'
    import c13 from '$lib/images/13.jpg'
    import c14 from '$lib/images/14.jpg'
    import c15 from '$lib/images/15.jpg'
    import c16 from '$lib/images/16.jpg'
    import c17 from '$lib/images/17.jpg'
    import c18 from '$lib/images/18.jpg'
    import c19 from '$lib/images/19.jpg'
    import c20 from '$lib/images/20.jpg'
    import c21 from '$lib/images/21.jpg'
    import c22 from '$lib/images/22.jpg'
    import c23 from '$lib/images/23.jpg'
    import c24 from '$lib/images/24.jpg'
    import c25 from '$lib/images/25.jpg'
    import c26 from '$lib/images/26.jpg'
    import c27 from '$lib/images/27.jpg'
    import c28 from '$lib/images/28.jpg'
    import c29 from '$lib/images/29.jpg'
    import c30 from '$lib/images/30.jpg'
    import c31 from '$lib/images/31.jpg'
    import c32 from '$lib/images/32.jpg'
    import c33 from '$lib/images/33.jpg'
    import c34 from '$lib/images/34.jpg'
    import c35 from '$lib/images/35.jpg'
    import c36 from '$lib/images/36.jpg'
    import c37 from '$lib/images/37.jpg'
    import c38 from '$lib/images/38.jpg'
    import c39 from '$lib/images/39.jpg'
    import c40 from '$lib/images/40.jpg'
    import c41 from '$lib/images/41.jpg'
    import c42 from '$lib/images/42.jpg'
    import c43 from '$lib/images/43.jpg'
    import c44 from '$lib/images/44.jpg'
    import c45 from '$lib/images/45.jpg'
    import c46 from '$lib/images/46.jpg'
    import c47 from '$lib/images/47.jpg'
    import c48 from '$lib/images/48.jpg'
    import c49 from '$lib/images/49.jpg'
    import c50 from '$lib/images/50.jpg'
    import c51 from '$lib/images/51.jpg'
    import c52 from '$lib/images/52.jpg'
    import c53 from '$lib/images/53.jpg'
    import c54 from '$lib/images/54.jpg'
    import c55 from '$lib/images/55.jpg'
    import c56 from '$lib/images/56.jpg'
    import c57 from '$lib/images/57.jpg'
    import c58 from '$lib/images/58.jpg'
    import c59 from '$lib/images/59.jpg'
    import c60 from '$lib/images/60.jpg'
    import c61 from '$lib/images/61.jpg'
    import c62 from '$lib/images/62.jpg'
    import c63 from '$lib/images/63.jpg'
    import c64 from '$lib/images/64.jpg'
    import c65 from '$lib/images/65.jpg'
    import c66 from '$lib/images/66.jpg'
    import c67 from '$lib/images/67.jpg'
    import c68 from '$lib/images/68.jpg'
    import c69 from '$lib/images/69.jpg'
    import c70 from '$lib/images/70.jpg'
    import c71 from '$lib/images/71.jpg'
    import c72 from '$lib/images/72.jpg'
    import c73 from '$lib/images/73.jpg'
    import c74 from '$lib/images/74.jpg'
    import c75 from '$lib/images/75.jpg'
    import c76 from '$lib/images/76.jpg'
    import c77 from '$lib/images/77.jpg'
    const images = [
        c0, c1, c2, c3, c4, c5, c6, c7, c8, c9,
        c10, c11, c12, c13, c14, c15, c16, c17, c18, c19,
        c20, c21, c22, c23, c24, c25, c26, c27, c28, c29,
        c30, c31, c32, c33, c34, c35, c36, c37, c38, c39,
        c40, c41, c42, c43, c44, c45, c46, c47, c48, c49,
        c50, c51, c52, c53, c54, c55, c56, c57, c58, c59,
        c60, c61, c62, c63, c64, c65, c66, c67, c68, c69,
        c70, c71, c72, c73, c74, c75, c76, c77
    ];
    console.log(images)
    import { fly, fade, scale } from 'svelte/transition'
    import { flip } from 'svelte/animate';
    import { draw } from 'svelte/transition';
    import { quintOut } from 'svelte/easing';
    var i1, i2, i3;
    const tarot_deck = [
        "The Fool",
        "The Magician",
        "The High Priestess",
        "The Empress",
        "The Emperor",
        "The Hierophant",
        "The Lovers",
        "The Chariot",
        "Strength",
        "The Hermit",
        "The Wheel of Fortune",
        "Justice",
        "The Hanged Man",
        "Death",
        "Temperance",
        "The Devil",
        "The Tower",
        "The Star",
        "The Moon",
        "The Sun",
        "Judgement",
        "The World",
        "Two of Cups",
        "Three of Cups",
        "Four of Cups",
        "Five of Cups",
        "Six of Cups",
        "Seven of Cups",
        "Eight of Cups",
        "Nine of Cups",
        "Ten of Cups",
        "Ace of Cups",
        "King of Cups",
        "Knight of Cups",
        "Page of Cups",
        "Queen of Cups",
        "Two of Pentacles",
        "Three of Pentacles",
        "Four of Pentacles",
        "Five of Pentacles",
        "Six of Pentacles",
        "Seven of Pentacles",
        "Eight of Pentacles",
        "Nine of Pentacles",
        "Ten of Pentacles",
        "Ace of Pentacles",
        "King of Pentacles",
        "Knight of Pentacles",
        "Page of Pentacles",
        "Queen of Pentacles",
        "Two of Swords",
        "Three of Swords",
        "Four of Swords",
        "Five of Swords",
        "Six of Swords",
        "Seven of Swords",
        "Eight of Swords",
        "Nine of Swords",
        "Ten of Swords",
        "Ace of Swords",
        "King of Swords",
        "Knight of Swords",
        "Page of Swords",
        "Queen of Swords",
        "Two of Wands",
        "Three of Wands",
        "Four of Wands",
        "Five of Wands",
        "Six of Wands",
        "Seven of Wands",
        "Eight of Wands",
        "Nine of Wands",
        "Ten of Wands",
        "Ace of Wands",
        "King of Wands",
        "Knight of Wands",
        "Page of Wands",
        "Queen of Wands"
    ]
    function getImageByCardName(card: string): string {
        return images[get_index_of_card(card)]
    }

    let question: string
    let cards: string[] = []
    let stage = 0
    let reading_result: ReadingResult
    const loading_messages = ["Polishing crystal balls", "Sharpening magic wands", "Knocking on the tarot deck"]
    let loading_message_idx = 0
    console.log(images[get_index_of_card("Page of Wands")])
    setInterval(() => {
        loading_message_idx = (loading_message_idx + 1) % loading_messages.length
    }, 2000)

    class CardInterpretation {
        card: string
        interpretation: string
    }
    
    class ReadingResult {
        cards: CardInterpretation[]
        summary: string
        advice: string[]
    }

    class ReadingResultFactory {
        async getReadingResult(question: string): Promise<ReadingResult> {
            cards = generate_cards(3)
            console.log(cards[0])
            console.log(tarot_deck.findIndex((c) => c===cards[0]))

            i1 = images[tarot_deck.findIndex((c) => c===cards[0])]
            i2 = images[tarot_deck.findIndex((c) => c===cards[1])]
            i3 = images[tarot_deck.findIndex((c) => c===cards[2])]
            console.log(i1, i2, i3)
            const url = "http://127.0.0.1:8000/generate?"

            return await fetch(url + new URLSearchParams({
                card1: cards[0],
                card2: cards[1],
                card3: cards[2],
                question: question
            })).then((url) => url.json())
        }
    }

    async function processReadingRequest() {
        stage += 1
        reading_result = await new ReadingResultFactory().getReadingResult(question)
        stage += 1
    }


</script>
<div class="hidden fixed">
    <img class=" w-[200px] " src={ball}>
    <img class=" w-[200px] " src={i1}>
    <img class=" w-[200px] " src={i2}>
    <img class=" w-[200px] " src={i3}>
</div>
<img src={cloud2} class="absolute w-[100vw] h-[100vh] pointer-events-none">

<div class="flex w-[100vw] h-[100vh]">
    {#if stage === 0}
            <form  class="flex  gap-3 w-full m-auto items-center align-center justify-center z-20">
                <input class="bg-zinc-900 w-2/3 text-4xl text-white rounded p-4 bg-transparent outline-white outline" placeholder="What are you thinking about?" bind:value={question} type="text">
                <button type="submit" on:click={processReadingRequest} class="bg-purple-800 text-white text-4xl rounded p-6 outline outline-white hover:bg-purple-400 duration-150">🔮</button>
            </form>
    {:else if stage === 1 }
<!--        <div class="absolute m-auto bottom-0"><img src={ball}></div>-->
        <div class="flex relative flex-col gap-3 w-full m-auto items-center align-center justify-center z-20">
            <img use:lazyImage class=" w-[200px] " data-src={ball}>
            <h1 class="text-5xl text-white">{loading_messages[loading_message_idx]}</h1>
        </div>
    {:else if stage === 2}
        <div   class="flex flex-row gap-3 w-[75%] m-auto z-20">
            <div class="bg-zinc-900 rounded p-4 outline outline-white w-full h-full flex justify-center align-center items-center">
                <img  use:lazyImage class="m-auto" data-src={i1}>
            </div>
            <div class="rounded p-4 bg-zinc-900 outline outline-white text-white flex flex-col text-center items-center justify-center align-center ">
                <h1 class="text-6xl pb-4">{reading_result.cards[0].card}</h1>
                <p class="text-2xl text-left"> {reading_result.cards[0].interpretation}</p>
            </div>
        </div>

        <button on:click={() => stage++} class="fixed bottom-0 right-0 p-4 bg-purple-400 hover:bg-purple-500 transition-150 outline outline-white text-3xl text-white">Continue</button>
    {:else if stage === 3}
        <div class="flex flex-row gap-3 w-[75%] m-auto z-20">
            <div class="bg-zinc-900 rounded p-4 outline outline-white w-full h-full flex justify-center align-center items-center">
                <img use:lazyImage class="m-auto" data-src={i2}>
            </div>
            <div class="rounded p-4 bg-zinc-900 outline outline-white text-white flex flex-col text-center items-center justify-center align-center ">
                <h1 class="text-6xl pb-4">{reading_result.cards[1].card}</h1>
                <p class="text-2xl text-left"> {reading_result.cards[1].interpretation}</p>
            </div>
        </div>

        <button on:click={() => stage++} class="fixed bottom-0 right-0 p-4 bg-purple-400 hover:bg-purple-500 transition-150 outline outline-white text-3xl text-white">Continue</button>
    {:else if stage === 4}
        <div class="flex flex-row gap-3 w-[75%] m-auto z-20">
            <div class="bg-zinc-900 rounded p-4 outline outline-white w-full h-full flex justify-center align-center items-center">
                <img use:lazyImage class="m-auto" data-src={i3}>
            </div>
            <div class="rounded p-4 bg-zinc-900 outline outline-white text-white flex flex-col text-center items-center justify-center align-center ">
                <h1 class="text-6xl pb-4">{reading_result.cards[2].card}</h1>
                <p class="text-2xl text-left"> {reading_result.cards[2].interpretation}</p>
            </div>
        </div>

        <button on:click={() => stage++} class="fixed bottom-0 right-0 p-4 bg-purple-400 hover:bg-purple-500 transition-150 outline outline-white text-3xl text-white">Continue</button>
    {:else if stage === 5}
        <div class="flex flex-row gap-3 w-[75%] m-auto z-20">
            <div class="rounded p-4 p-4 bg-zinc-900 outline outline-white text-white flex flex-col text-center items-center justify-center align-center ">
                <h1 class="text-6xl pb-4">Summary</h1>
                <p class="text-2xl text-left">{reading_result.summary}</p>
            </div>
        </div>

        <button on:click={() => stage++} class="fixed bottom-0 right-0 p-4 bg-purple-400 hover:bg-purple-500 transition-150 outline outline-white text-3xl text-white">Continue</button>

    {:else if stage === 6}
        <div  class="flex flex-row gap-3 w-[75%] m-auto z-20">
            <div class="rounded p-8 bg-zinc-900 outline outline-white text-white flex flex-col text-center items-center justify-center align-center ">
                <h1 class="text-6xl pb-4">Here is some advice based on the reading:</h1>
                <ul class=" list-disc ">
                    {#each reading_result.advice as advice}
                        <li class="text-left text-2xl">{advice}</li>
                    {/each}
                </ul>
            </div>
        </div>

    {/if}
</div>


<style>
    h1 {
        font-family: "Brasika";
    }
</style>