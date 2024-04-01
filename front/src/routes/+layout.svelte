<script>

	import './styles.css';
    export const prerender = true;

</script>

<div class="app">
	<main>
		<slot />
	</main>
</div>

<style>

	@font-face {
		font-family: 'Lora';
		font-style: normal;
		font-weight: 800;
		src: url('/papyrus.ttf');
	}

	@font-face {
		font-family: 'Brasika';
		font-style: normal;
		font-weight: 800;
		src: url('/brasika.otf');
	}


	.app {
		/*display: flex;*/
		/*flex-direction: column;*/
		/*min-height: 100vh;*/
		background: url("$lib/images/stars2.gif"), linear-gradient(0deg, rgba(172, 110, 219, 1) 0%, rgba(205, 103, 208, 1) 100%), linear-gradient(0deg, rgba(172, 110, 219, 1) 34%, rgba(205, 103, 208, 0) 100%);
		font-family: 'Antic';
	}
	h1 {
		font-family: "Brasika";
	}
	/*main {*/
	/*	flex: 1;*/
	/*	display: flex;*/
	/*	flex-direction: column;*/
	/*	padding: 1rem;*/
	/*	width: 100%;*/
	/*	max-width: 64rem;*/
	/*	margin: 0 auto;*/
	/*	box-sizing: border-box;*/
	/*}*/


</style>
