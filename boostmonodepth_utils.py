<!DOCTYPE html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta
			name="viewport"
			content="width=device-width, initial-scale=1.0, user-scalable=no"
		/>
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta property="og:title" content="boostmonodepth_utils.py · Epoching/3D_Photo_Inpainting at main" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/spaces/Epoching/3D_Photo_Inpainting/blob/main/boostmonodepth_utils.py" />
		<meta property="og:image" content="https://huggingface.co/front/thumbnails/v2-2.png" />

		<link rel="stylesheet" href="/front/build/style.f418ef775.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>
		<link
			rel="stylesheet"
			href="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.css"
		/>

		 

		<title>boostmonodepth_utils.py · Epoching/3D_Photo_Inpainting at main</title>
	</head>
	<body
		class="flex flex-col min-h-screen bg-white dark:bg-gray-950 text-black ViewerBlobPage"
	>
		<div class="flex flex-col min-h-screen ">
	<div class="SVELTE_HYDRATER contents" data-props="{&quot;apiInferenceUrl&quot;:&quot;https://api-inference.huggingface.co&quot;,&quot;hfCloudName&quot;:&quot;private&quot;,&quot;isAuth&quot;:false,&quot;isHfCloud&quot;:false,&quot;isWide&quot;:false}" data-target="MainHeader"><header class="border-b border-gray-100"><div class="w-full px-4 lg:px-6 xl:container flex items-center h-16"><div class="flex flex-1 items-center"><a class="flex flex-none items-center mr-5 lg:mr-6" href="/"><img alt="Hugging Face's logo" class="md:mr-2 w-7" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden text-lg font-bold whitespace-nowrap md:block">Hugging Face</span></a>
			
			<div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 lg:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 
			form-input-alt h-9 pl-8 pr-3 focus:shadow-xl" name="" placeholder="Search models, datasets, users..."  spellcheck="false" type="text">
	<svg class="absolute left-2.5 top-2.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div>
			<button class="lg:hidden relative flex-none place-self-stretch flex items-center justify-center w-8" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="22" height="22" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M4 24h24v2H4z"></path><path d="M4 12h24v2H4z"></path><path d="M4 18h24v2H4z"></path><path d="M4 6h24v2H4z"></path></svg></button>

</div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center space-x-2"><li><a class="flex items-center group px-2 py-0.5 dark:hover:text-gray-400 hover:text-indigo-700" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
					Models</a>
			</li><li><a class="flex items-center group px-2 py-0.5 dark:hover:text-gray-400 hover:text-red-700" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					Datasets</a>
			</li><li><a class="flex items-center group px-2 py-0.5 dark:hover:text-gray-400 hover:text-blue-700" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
					Spaces</a>
			</li><li><a class="flex items-center group px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path opacity="0.5" d="M20.9022 5.10334L10.8012 10.8791L7.76318 9.11193C8.07741 8.56791 8.5256 8.11332 9.06512 7.7914L15.9336 3.73907C17.0868 3.08811 18.5002 3.26422 19.6534 3.91519L19.3859 3.73911C19.9253 4.06087 20.5879 4.56025 20.9022 5.10334Z" fill="currentColor"></path><path d="M10.7999 10.8792V28.5483C10.2136 28.5475 9.63494 28.4139 9.10745 28.1578C8.5429 27.8312 8.074 27.3621 7.74761 26.7975C7.42122 26.2327 7.24878 25.5923 7.24756 24.9402V10.9908C7.25062 10.3319 7.42358 9.68487 7.74973 9.1123L10.7999 10.8792Z" fill="currentColor" fill-opacity="0.75"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M21.3368 10.8499V6.918C21.3331 6.25959 21.16 5.61234 20.8346 5.03949L10.7971 10.8727L10.8046 10.874L21.3368 10.8499Z" fill="currentColor"></path><path opacity="0.5" d="M21.7937 10.8488L10.7825 10.8741V28.5486L21.7937 28.5234C23.3344 28.5234 24.5835 27.2743 24.5835 25.7335V13.6387C24.5835 12.0979 23.4365 11.1233 21.7937 10.8488Z" fill="currentColor"></path></svg>
					Docs</a>
			</li>
		<li><div class="relative ">
	<button class="px-2 py-0.5 group hover:text-green-700 dark:hover:text-gray-400 flex items-center
			" type="button">
		<svg class="mr-1.5 text-gray-400 group-hover:text-green-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M19 6H5a3 3 0 0 0-3 3v2.72L8.837 14h6.326L22 11.72V9a3 3 0 0 0-3-3z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M10 6V5h4v1h2V5a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v1h2zm-1.163 8L2 11.72V18a3.003 3.003 0 0 0 3 3h14a3.003 3.003 0 0 0 3-3v-6.28L15.163 14H8.837z" fill="currentColor"></path></svg>
			Solutions
		</button>
	
	
	
	</div></li>

			<li><a class="flex items-center group px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/pricing" data-ga-category="header-menu" data-ga-action="clicked pricing" data-ga-label="pricing">Pricing
				</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center
			" type="button">
		<svg class="mr-1.5 text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
		</button>
	
	
	
	</div></li>
		<li><hr class="w-0.5 h-5 border-none bg-gray-100 dark:bg-gray-800"></li>
		
			<li><a class="px-2 py-0.5 block cursor-pointer hover:text-gray-500 dark:hover:text-gray-400" href="/login">Log In
				</a></li>
			<li><a class="ml-2 btn" href="/join">Sign Up </a></li></ul></nav></div></header></div>
	
	
	<main class="flex flex-col flex-1 "><header class="bg-gradient-to-t from-gray-50-to-white via-white dark:via-gray-950 
		pt-4 "><div class="container relative"><h1 class="flex items-center flex-wrap text-lg leading-tight 
				"><a href="/spaces" class="group flex items-center mb-1"><svg class="mr-1 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M7.80914 18.7462V24.1907H13.2536V18.7462H7.80914Z" fill="#FF3270"></path><path d="M18.7458 18.7462V24.1907H24.1903V18.7462H18.7458Z" fill="#861FFF"></path><path d="M7.80914 7.80982V13.2543H13.2536V7.80982H7.80914Z" fill="#097EFF"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M4 6.41775C4 5.08246 5.08246 4 6.41775 4H14.6457C15.7626 4 16.7026 4.75724 16.9802 5.78629C18.1505 4.67902 19.7302 4 21.4685 4C25.0758 4 28.0003 6.92436 28.0003 10.5317C28.0003 12.27 27.3212 13.8497 26.2139 15.02C27.243 15.2977 28.0003 16.2376 28.0003 17.3545V25.5824C28.0003 26.9177 26.9177 28.0003 25.5824 28.0003H17.0635H14.9367H6.41775C5.08246 28.0003 4 26.9177 4 25.5824V15.1587V14.9367V6.41775ZM7.80952 7.80952V13.254H13.254V7.80952H7.80952ZM7.80952 24.1907V18.7462H13.254V24.1907H7.80952ZM18.7462 24.1907V18.7462H24.1907V24.1907H18.7462ZM18.7462 10.5317C18.7462 9.0283 19.9651 7.80952 21.4685 7.80952C22.9719 7.80952 24.1907 9.0283 24.1907 10.5317C24.1907 12.0352 22.9719 13.254 21.4685 13.254C19.9651 13.254 18.7462 12.0352 18.7462 10.5317Z" fill="black"></path><path d="M21.4681 7.80982C19.9647 7.80982 18.7458 9.02861 18.7458 10.5321C18.7458 12.0355 19.9647 13.2543 21.4681 13.2543C22.9715 13.2543 24.1903 12.0355 24.1903 10.5321C24.1903 9.02861 22.9715 7.80982 21.4681 7.80982Z" fill="#FFD702"></path></svg>
					<span class="text-gray-400 group-hover:text-gray-500 mr-3 font-semibold">Spaces:</span></a>
			<div class="flex items-center mb-1"><img alt="" class="w-4 h-4 rounded-full mr-1.5" src="https://aeiljuispo.cloudimg.io/v7/https://s3.amazonaws.com/moonup/production/uploads/1625651487569-noauth.png?w=200&amp;h=200&amp;f=face">
					<a href="/Epoching" class="font-sans text-gray-400 hover:text-blue-600">Epoching</a>
					<div class="text-gray-300 mx-0.5">/</div></div>
			<div class="max-w-full mb-1"><a class="font-mono font-semibold break-words" href="/spaces/Epoching/3D_Photo_Inpainting">3D_Photo_Inpainting</a>
				<div class="SVELTE_HYDRATER contents" data-props="{&quot;classNames&quot;:&quot;mr-4&quot;,&quot;title&quot;:&quot;Copy space name to clipboard&quot;,&quot;value&quot;:&quot;Epoching/3D_Photo_Inpainting&quot;}" data-target="CopyButton"><button class="inline-flex items-center relative bg-white text-sm focus:text-green-500  cursor-pointer focus:outline-none
		mr-4
		mx-0.5
		
		
		text-gray-600
		
	" title="Copy space name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	<div class="
		absolute pointer-events-none transition-opacity bg-black text-white py-1 px-2 leading-tight rounded font-normal shadow 
		left-1/2 top-full transform -translate-x-1/2 translate-y-2
		opacity-0
	"><div class="absolute bottom-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-black border-4 border-t-0" style="
				border-left-color: transparent;
				border-right-color: transparent;
			"></div>
	Copied</div></button></div></div>
			<div class="SVELTE_HYDRATER contents" data-props="{&quot;classNames&quot;:&quot;mr-3 mb-1&quot;,&quot;isLikedByUser&quot;:false,&quot;likes&quot;:14,&quot;repoId&quot;:&quot;Epoching/3D_Photo_Inpainting&quot;,&quot;repoType&quot;:&quot;space&quot;}" data-target="LikeButton"><div class="inline-flex items-center border leading-none whitespace-nowrap text-sm rounded-md text-gray-500 overflow-hidden bg-white
		 mr-3 mb-1"><button class="relative flex items-center px-1.5 py-1 hover:bg-gradient-to-t focus:outline-none from-red-50 to-transparent dark:from-red-900 dark:to-red-800 overflow-hidden"  title="Like"><svg class="mr-1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		<svg class="mr-1 absolute text-red-500 origin-center transform transition ease-in\n\t\t\t\ttranslate-y-10 scale-0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.5,4c-2,0-3.9,0.8-5.3,2.2L16,7.4l-1.1-1.1C12,3.3,7.2,3.3,4.3,6.2c0,0-0.1,0.1-0.1,0.1c-3,3-3,7.8,0,10.8L16,29l11.8-11.9c3-3,3-7.8,0-10.8C26.4,4.8,24.5,4,22.5,4z"></path></svg>
		like
	</button>
	<button class="flex items-center px-1.5 py-1 border-l text-gray-400 focus:outline-none hover:bg-gray-50 dark:hover:bg-gray-700 focus:bg-gray-100 " title="See users who liked this repository">14</button></div>
</div>
			<div class="SVELTE_HYDRATER contents" data-props="{&quot;initStage&quot;:&quot;runtime_error&quot;,&quot;rights&quot;:{&quot;readRepoContent&quot;:false,&quot;writeRepoContent&quot;:false,&quot;readRepoSettings&quot;:false,&quot;writeRepoSettings&quot;:false,&quot;readOrgSettings&quot;:false,&quot;writeOrgSettings&quot;:false},&quot;spaceId&quot;:&quot;Epoching/3D_Photo_Inpainting&quot;}" data-target="SpaceStatus">

	<div class="border inline-flex items-center leading-none whitespace-nowrap px-1.5 py-[0.3rem] font-mono text-xs rounded-md text-gray-400 overflow-hidden bg-white mr-3 mb-1 select-none
		border-red-200 bg-red-50"><div class="inline-block h-1.5 w-1.5 rounded-full ml-0.5 mr-1.5 animate-pulse bg-red-500 "></div>
		<span class="text-red-500">Runtime error</span></div></div></h1>
		
		<div class="border-b border-gray-100"><div class="flex flex-col-reverse lg:flex-row lg:items-center lg:justify-between"><div class="flex items-center h-12 -mb-px overflow-x-auto overflow-y-hidden"><a class="tab-alternate " href="/spaces/Epoching/3D_Photo_Inpainting"><svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
			App
		</a>
		<a class="tab-alternate active" href="/spaces/Epoching/3D_Photo_Inpainting/tree/main"><svg class="mr-1.5 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
			Files and versions
		</a>
		</div>
				<div class="SVELTE_HYDRATER contents" data-props="{&quot;linkedModels&quot;:[],&quot;linkedDatasets&quot;:[]}" data-target="SpaceHeaderActions">


<div class="relative mb-1.5 mt-1.5 space-y-1 sm:flex sm:space-y-0 sm:space-x-1.5 lg:mb-0 lg:mt-0">
	</div></div>
	</div></div></div></header>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full
	md:grid-cols-12
	 
		space-y-4
		md:gap-6
		mb-16
	"><section class="pt-8 border-gray-100 col-span-full"><header class="pb-2 flex items-center justify-between flex-wrap"><div class="flex flex-wrap items-center"><div class="SVELTE_HYDRATER contents" data-props="{&quot;path&quot;:&quot;boostmonodepth_utils.py&quot;,&quot;repoName&quot;:&quot;Epoching/3D_Photo_Inpainting&quot;,&quot;repoType&quot;:&quot;space&quot;,&quot;rev&quot;:&quot;main&quot;,&quot;refs&quot;:{&quot;branches&quot;:[&quot;main&quot;],&quot;tags&quot;:[]},&quot;view&quot;:&quot;blob&quot;}" data-target="BranchSelector"><div class="relative mr-4 mb-2">
	<button class="text-base
			cursor-pointer w-full btn text-sm" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M7 10l5 5l5-5z" fill="currentColor"></path></svg></button>
	
	
	
	</div></div>
		<div class="flex items-center flex-wrap mb-2"><a class="hover:underline text-gray-800" href="/spaces/Epoching/3D_Photo_Inpainting/tree/main">3D_Photo_Inpainting</a>
			<span class="text-gray-300 mx-1 font-light">/</span>
				<span class="font-light dark:text-gray-300">boostmonodepth_utils.py</span>

			</div></div>

	<div class="flex flex-row items-center mb-2">
		</div></header>
			<div class="border border-b-0 dark:border-gray-800 px-3 py-2 flex items-baseline rounded-t-lg bg-gradient-to-t from-gray-100-to-white">
			<div class="mr-5 truncate flex items-center flex-none">Saini
				
			</div>
		<a class="mr-4 font-mono text-sm text-gray-500 truncate hover:underline" href="/spaces/Epoching/3D_Photo_Inpainting/commit/0b9f920d474162c2b7cadcb1af41b52fcad14f87">init</a>
		<a class="text-sm border dark:border-gray-800 px-1.5 rounded bg-gray-50 dark:bg-gray-900 hover:underline" href="/spaces/Epoching/3D_Photo_Inpainting/commit/0b9f920d474162c2b7cadcb1af41b52fcad14f87">0b9f920</a>
		

		<time class="ml-auto hidden lg:block text-gray-500 dark:text-gray-400 truncate flex-none pl-2" datetime="2021-12-21T12:45:25" title="Tue, 21 Dec 2021 12:45:25 GMT">3 months ago</time></div>
			<div class="flex flex-wrap items-center justify-between px-3 py-1.5 border dark:border-gray-800 text-sm text-gray-800 dark:bg-gray-900"><div class="flex flex-wrap items-center"><a class="flex items-center hover:underline my-1 mr-4" href="/spaces/Epoching/3D_Photo_Inpainting/raw/main/boostmonodepth_utils.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
								raw
							</a><a class="flex items-center hover:underline my-1 mr-4" href="/spaces/Epoching/3D_Photo_Inpainting/commits/main/boostmonodepth_utils.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
								history
							</a><a class="flex items-center hover:underline my-1 mr-4" href="/spaces/Epoching/3D_Photo_Inpainting/blame/main/boostmonodepth_utils.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
								blame
							</a>
					<div class="text-gray-400 flex items-center"><svg class="text-gray-300 text-sm mr-1.5 -translate-y-px" width="1em" height="1em" viewBox="0 0 22 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.3634 10.3639C15.8486 10.8491 15.8486 11.6357 15.3634 12.1209L10.9292 16.5551C10.6058 16.8785 10.0814 16.8785 9.7579 16.5551L7.03051 13.8277C6.54532 13.3425 6.54532 12.5558 7.03051 12.0707C7.51569 11.5855 8.30234 11.5855 8.78752 12.0707L9.7579 13.041C10.0814 13.3645 10.6058 13.3645 10.9292 13.041L13.6064 10.3639C14.0916 9.8787 14.8782 9.8787 15.3634 10.3639Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6666 27.12C4.93329 25.28 0 19.2267 0 12.7867V6.52001C0 5.40001 0.693334 4.41334 1.73333 4.01334L9.73333 1.01334C10.3333 0.786673 11 0.786673 11.6 1.02667L19.6 4.02667C20.1083 4.21658 20.5465 4.55701 20.8562 5.00252C21.1659 5.44803 21.3324 5.97742 21.3333 6.52001V12.7867C21.3333 19.24 16.4 25.28 10.6666 27.12Z" fill="currentColor" fill-opacity="0.22"></path><path d="M10.0845 1.94967L10.0867 1.94881C10.4587 1.8083 10.8666 1.81036 11.2286 1.95515L11.2387 1.95919L11.2489 1.963L19.2489 4.963L19.25 4.96342C19.5677 5.08211 19.8416 5.29488 20.0351 5.57333C20.2285 5.85151 20.3326 6.18203 20.3333 6.52082C20.3333 6.52113 20.3333 6.52144 20.3333 6.52176L20.3333 12.7867C20.3333 18.6535 15.8922 24.2319 10.6666 26.0652C5.44153 24.2316 1 18.6409 1 12.7867V6.52001C1 5.82357 1.42893 5.20343 2.08883 4.94803L10.0845 1.94967Z" stroke="currentColor" stroke-opacity="0.30" stroke-width="2"></path></svg>

								Safe
							</div></div>
				<div class="dark:text-gray-300">2.27 kB</div></div>

			<div class="border border-t-0 rounded-b-lg dark:bg-gray-925 dark:border-gray-800 leading-tight"><div class="py-3"><div class="SVELTE_HYDRATER contents" data-props="{&quot;lines&quot;:[&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;import&lt;/span&gt; os&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;import&lt;/span&gt; cv2&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;import&lt;/span&gt; glob&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;import&lt;/span&gt; numpy &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;as&lt;/span&gt; np&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;import&lt;/span&gt; imageio&quot;,&quot;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;from&lt;/span&gt; MiDaS.MiDaS_utils &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;import&lt;/span&gt; write_depth&quot;,&quot;&quot;,&quot;BOOST_BASE = &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;BoostingMonocularDepth&amp;#x27;&lt;/span&gt;&quot;,&quot;&quot;,&quot;BOOST_INPUTS = &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;inputs&amp;#x27;&lt;/span&gt;&quot;,&quot;BOOST_OUTPUTS = &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;outputs&amp;#x27;&lt;/span&gt;&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-function\\&quot;&gt;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;def&lt;/span&gt; &lt;span class=\\&quot;hljs-title\\&quot;&gt;run_boostmonodepth&lt;/span&gt;(&lt;span class=\\&quot;hljs-params\\&quot;&gt;img_names, src_folder, depth_folder&lt;/span&gt;):&lt;/span&gt;&quot;,&quot;&quot;,&quot;    &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;if&lt;/span&gt; &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;not&lt;/span&gt; &lt;span class=\\&quot;hljs-built_in\\&quot;&gt;isinstance&lt;/span&gt;(img_names, &lt;span class=\\&quot;hljs-built_in\\&quot;&gt;list&lt;/span&gt;):&quot;,&quot;        img_names = [img_names]&quot;,&quot;&quot;,&quot;    &lt;span class=\\&quot;hljs-comment\\&quot;&gt;# remove irrelevant files first&lt;/span&gt;&quot;,&quot;    clean_folder(os.path.join(BOOST_BASE, BOOST_INPUTS))&quot;,&quot;    clean_folder(os.path.join(BOOST_BASE, BOOST_OUTPUTS))&quot;,&quot;&quot;,&quot;    tgt_names = []&quot;,&quot;    &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;for&lt;/span&gt; img_name &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;in&lt;/span&gt; img_names:&quot;,&quot;        base_name = os.path.basename(img_name)&quot;,&quot;        tgt_name = os.path.join(BOOST_BASE, BOOST_INPUTS, base_name)&quot;,&quot;        os.system(&lt;span class=\\&quot;hljs-string\\&quot;&gt;f&amp;#x27;cp &lt;span class=\\&quot;hljs-subst\\&quot;&gt;{img_name}&lt;/span&gt; &lt;span class=\\&quot;hljs-subst\\&quot;&gt;{tgt_name}&lt;/span&gt;&amp;#x27;&lt;/span&gt;)&quot;,&quot;&quot;,&quot;        &lt;span class=\\&quot;hljs-comment\\&quot;&gt;# keep only the file name here.&lt;/span&gt;&quot;,&quot;        &lt;span class=\\&quot;hljs-comment\\&quot;&gt;# they save all depth as .png file&lt;/span&gt;&quot;,&quot;        tgt_names.append(os.path.basename(tgt_name).replace(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;.jpg&amp;#x27;&lt;/span&gt;, &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;.png&amp;#x27;&lt;/span&gt;))&quot;,&quot;&quot;,&quot;    os.system(&lt;span class=\\&quot;hljs-string\\&quot;&gt;f&amp;#x27;cd &lt;span class=\\&quot;hljs-subst\\&quot;&gt;{BOOST_BASE}&lt;/span&gt; &amp;amp;&amp;amp; python run.py --Final --data_dir &lt;span class=\\&quot;hljs-subst\\&quot;&gt;{BOOST_INPUTS}&lt;/span&gt;/  --output_dir &lt;span class=\\&quot;hljs-subst\\&quot;&gt;{BOOST_OUTPUTS}&lt;/span&gt; --depthNet 0&amp;#x27;&lt;/span&gt;)&quot;,&quot;&quot;,&quot;    &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;for&lt;/span&gt; i, (img_name, tgt_name) &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;in&lt;/span&gt; &lt;span class=\\&quot;hljs-built_in\\&quot;&gt;enumerate&lt;/span&gt;(&lt;span class=\\&quot;hljs-built_in\\&quot;&gt;zip&lt;/span&gt;(img_names, tgt_names)):&quot;,&quot;        img = imageio.imread(img_name)&quot;,&quot;        H, W = img.shape[:&lt;span class=\\&quot;hljs-number\\&quot;&gt;2&lt;/span&gt;]&quot;,&quot;        scale = &lt;span class=\\&quot;hljs-number\\&quot;&gt;640.&lt;/span&gt; / &lt;span class=\\&quot;hljs-built_in\\&quot;&gt;max&lt;/span&gt;(H, W)&quot;,&quot;&quot;,&quot;        &lt;span class=\\&quot;hljs-comment\\&quot;&gt;# resize and save depth&lt;/span&gt;&quot;,&quot;        target_height, target_width = &lt;span class=\\&quot;hljs-built_in\\&quot;&gt;int&lt;/span&gt;(&lt;span class=\\&quot;hljs-built_in\\&quot;&gt;round&lt;/span&gt;(H * scale)), &lt;span class=\\&quot;hljs-built_in\\&quot;&gt;int&lt;/span&gt;(&lt;span class=\\&quot;hljs-built_in\\&quot;&gt;round&lt;/span&gt;(W * scale))&quot;,&quot;        depth = imageio.imread(os.path.join(BOOST_BASE, BOOST_OUTPUTS, tgt_name))&quot;,&quot;        depth = np.array(depth).astype(np.float32)&quot;,&quot;        depth = resize_depth(depth, target_width, target_height)&quot;,&quot;        np.save(os.path.join(depth_folder, tgt_name.replace(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;.png&amp;#x27;&lt;/span&gt;, &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;.npy&amp;#x27;&lt;/span&gt;)), depth / &lt;span class=\\&quot;hljs-number\\&quot;&gt;32768.&lt;/span&gt; - &lt;span class=\\&quot;hljs-number\\&quot;&gt;1.&lt;/span&gt;)&quot;,&quot;        write_depth(os.path.join(depth_folder, tgt_name.replace(&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;.png&amp;#x27;&lt;/span&gt;, &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;&amp;#x27;&lt;/span&gt;)), depth)&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-function\\&quot;&gt;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;def&lt;/span&gt; &lt;span class=\\&quot;hljs-title\\&quot;&gt;clean_folder&lt;/span&gt;(&lt;span class=\\&quot;hljs-params\\&quot;&gt;folder, img_exts=[&lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;.png&amp;#x27;&lt;/span&gt;, &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;.jpg&amp;#x27;&lt;/span&gt;, &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;#x27;.npy&amp;#x27;&lt;/span&gt;]&lt;/span&gt;):&lt;/span&gt;&quot;,&quot;&quot;,&quot;    &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;for&lt;/span&gt; img_ext &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;in&lt;/span&gt; img_exts:&quot;,&quot;        paths_to_check = os.path.join(folder, &lt;span class=\\&quot;hljs-string\\&quot;&gt;f&amp;#x27;*&lt;span class=\\&quot;hljs-subst\\&quot;&gt;{img_ext}&lt;/span&gt;&amp;#x27;&lt;/span&gt;)&quot;,&quot;        &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;if&lt;/span&gt; &lt;span class=\\&quot;hljs-built_in\\&quot;&gt;len&lt;/span&gt;(glob.glob(paths_to_check)) == &lt;span class=\\&quot;hljs-number\\&quot;&gt;0&lt;/span&gt;:&quot;,&quot;            &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;continue&lt;/span&gt;&quot;,&quot;        print(paths_to_check)&quot;,&quot;        os.system(&lt;span class=\\&quot;hljs-string\\&quot;&gt;f&amp;#x27;rm &lt;span class=\\&quot;hljs-subst\\&quot;&gt;{paths_to_check}&lt;/span&gt;&amp;#x27;&lt;/span&gt;)&quot;,&quot;&quot;,&quot;&lt;span class=\\&quot;hljs-function\\&quot;&gt;&lt;span class=\\&quot;hljs-keyword\\&quot;&gt;def&lt;/span&gt; &lt;span class=\\&quot;hljs-title\\&quot;&gt;resize_depth&lt;/span&gt;(&lt;span class=\\&quot;hljs-params\\&quot;&gt;depth, width, height&lt;/span&gt;):&lt;/span&gt;&quot;,&quot;    &lt;span class=\\&quot;hljs-string\\&quot;&gt;&amp;quot;&amp;quot;&amp;quot;Resize numpy (or image read by imageio) depth map&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-string\\&quot;&gt;&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-string\\&quot;&gt;    Args:&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-string\\&quot;&gt;        depth (numpy): depth&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-string\\&quot;&gt;        width (int): image width&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-string\\&quot;&gt;        height (int): image height&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-string\\&quot;&gt;&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-string\\&quot;&gt;    Returns:&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-string\\&quot;&gt;        array: processed depth&lt;/span&gt;&quot;,&quot;&lt;span class=\\&quot;hljs-string\\&quot;&gt;    &amp;quot;&amp;quot;&amp;quot;&lt;/span&gt;&quot;,&quot;    depth = cv2.blur(depth, (&lt;span class=\\&quot;hljs-number\\&quot;&gt;3&lt;/span&gt;, &lt;span class=\\&quot;hljs-number\\&quot;&gt;3&lt;/span&gt;))&quot;,&quot;    &lt;span class=\\&quot;hljs-keyword\\&quot;&gt;return&lt;/span&gt; cv2.resize(depth, (width, height), interpolation=cv2.INTER_AREA)&quot;,&quot;&quot;]}" data-target="BlobContent"><div class="relative text-sm"><div class="overflow-x-auto"><table class="border-collapse font-mono"><tbody><tr class="" id="L1"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">1</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">import</span> os</td>
					</tr><tr class="" id="L2"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">2</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">import</span> cv2</td>
					</tr><tr class="" id="L3"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">3</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">import</span> glob</td>
					</tr><tr class="" id="L4"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">4</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">import</span> numpy <span class="hljs-keyword">as</span> np</td>
					</tr><tr class="" id="L5"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">5</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">import</span> imageio</td>
					</tr><tr class="" id="L6"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">6</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-keyword">from</span> MiDaS.MiDaS_utils <span class="hljs-keyword">import</span> write_depth</td>
					</tr><tr class="" id="L7"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">7</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L8"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">8</td>
						<td class="px-3 overflow-visible whitespace-pre">BOOST_BASE = <span class="hljs-string">&#x27;BoostingMonocularDepth&#x27;</span></td>
					</tr><tr class="" id="L9"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">9</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L10"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">10</td>
						<td class="px-3 overflow-visible whitespace-pre">BOOST_INPUTS = <span class="hljs-string">&#x27;inputs&#x27;</span></td>
					</tr><tr class="" id="L11"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">11</td>
						<td class="px-3 overflow-visible whitespace-pre">BOOST_OUTPUTS = <span class="hljs-string">&#x27;outputs&#x27;</span></td>
					</tr><tr class="" id="L12"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">12</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L13"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">13</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">run_boostmonodepth</span>(<span class="hljs-params">img_names, src_folder, depth_folder</span>):</span></td>
					</tr><tr class="" id="L14"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">14</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L15"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">15</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> <span class="hljs-built_in">isinstance</span>(img_names, <span class="hljs-built_in">list</span>):</td>
					</tr><tr class="" id="L16"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">16</td>
						<td class="px-3 overflow-visible whitespace-pre">        img_names = [img_names]</td>
					</tr><tr class="" id="L17"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">17</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L18"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">18</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-comment"># remove irrelevant files first</span></td>
					</tr><tr class="" id="L19"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">19</td>
						<td class="px-3 overflow-visible whitespace-pre">    clean_folder(os.path.join(BOOST_BASE, BOOST_INPUTS))</td>
					</tr><tr class="" id="L20"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">20</td>
						<td class="px-3 overflow-visible whitespace-pre">    clean_folder(os.path.join(BOOST_BASE, BOOST_OUTPUTS))</td>
					</tr><tr class="" id="L21"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">21</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L22"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">22</td>
						<td class="px-3 overflow-visible whitespace-pre">    tgt_names = []</td>
					</tr><tr class="" id="L23"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">23</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-keyword">for</span> img_name <span class="hljs-keyword">in</span> img_names:</td>
					</tr><tr class="" id="L24"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">24</td>
						<td class="px-3 overflow-visible whitespace-pre">        base_name = os.path.basename(img_name)</td>
					</tr><tr class="" id="L25"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">25</td>
						<td class="px-3 overflow-visible whitespace-pre">        tgt_name = os.path.join(BOOST_BASE, BOOST_INPUTS, base_name)</td>
					</tr><tr class="" id="L26"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">26</td>
						<td class="px-3 overflow-visible whitespace-pre">        os.system(<span class="hljs-string">f&#x27;cp <span class="hljs-subst">{img_name}</span> <span class="hljs-subst">{tgt_name}</span>&#x27;</span>)</td>
					</tr><tr class="" id="L27"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">27</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L28"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">28</td>
						<td class="px-3 overflow-visible whitespace-pre">        <span class="hljs-comment"># keep only the file name here.</span></td>
					</tr><tr class="" id="L29"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">29</td>
						<td class="px-3 overflow-visible whitespace-pre">        <span class="hljs-comment"># they save all depth as .png file</span></td>
					</tr><tr class="" id="L30"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">30</td>
						<td class="px-3 overflow-visible whitespace-pre">        tgt_names.append(os.path.basename(tgt_name).replace(<span class="hljs-string">&#x27;.jpg&#x27;</span>, <span class="hljs-string">&#x27;.png&#x27;</span>))</td>
					</tr><tr class="" id="L31"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">31</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L32"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">32</td>
						<td class="px-3 overflow-visible whitespace-pre">    os.system(<span class="hljs-string">f&#x27;cd <span class="hljs-subst">{BOOST_BASE}</span> &amp;&amp; python run.py --Final --data_dir <span class="hljs-subst">{BOOST_INPUTS}</span>/  --output_dir <span class="hljs-subst">{BOOST_OUTPUTS}</span> --depthNet 0&#x27;</span>)</td>
					</tr><tr class="" id="L33"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">33</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L34"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">34</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-keyword">for</span> i, (img_name, tgt_name) <span class="hljs-keyword">in</span> <span class="hljs-built_in">enumerate</span>(<span class="hljs-built_in">zip</span>(img_names, tgt_names)):</td>
					</tr><tr class="" id="L35"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">35</td>
						<td class="px-3 overflow-visible whitespace-pre">        img = imageio.imread(img_name)</td>
					</tr><tr class="" id="L36"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">36</td>
						<td class="px-3 overflow-visible whitespace-pre">        H, W = img.shape[:<span class="hljs-number">2</span>]</td>
					</tr><tr class="" id="L37"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">37</td>
						<td class="px-3 overflow-visible whitespace-pre">        scale = <span class="hljs-number">640.</span> / <span class="hljs-built_in">max</span>(H, W)</td>
					</tr><tr class="" id="L38"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">38</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L39"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">39</td>
						<td class="px-3 overflow-visible whitespace-pre">        <span class="hljs-comment"># resize and save depth</span></td>
					</tr><tr class="" id="L40"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">40</td>
						<td class="px-3 overflow-visible whitespace-pre">        target_height, target_width = <span class="hljs-built_in">int</span>(<span class="hljs-built_in">round</span>(H * scale)), <span class="hljs-built_in">int</span>(<span class="hljs-built_in">round</span>(W * scale))</td>
					</tr><tr class="" id="L41"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">41</td>
						<td class="px-3 overflow-visible whitespace-pre">        depth = imageio.imread(os.path.join(BOOST_BASE, BOOST_OUTPUTS, tgt_name))</td>
					</tr><tr class="" id="L42"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">42</td>
						<td class="px-3 overflow-visible whitespace-pre">        depth = np.array(depth).astype(np.float32)</td>
					</tr><tr class="" id="L43"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">43</td>
						<td class="px-3 overflow-visible whitespace-pre">        depth = resize_depth(depth, target_width, target_height)</td>
					</tr><tr class="" id="L44"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">44</td>
						<td class="px-3 overflow-visible whitespace-pre">        np.save(os.path.join(depth_folder, tgt_name.replace(<span class="hljs-string">&#x27;.png&#x27;</span>, <span class="hljs-string">&#x27;.npy&#x27;</span>)), depth / <span class="hljs-number">32768.</span> - <span class="hljs-number">1.</span>)</td>
					</tr><tr class="" id="L45"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">45</td>
						<td class="px-3 overflow-visible whitespace-pre">        write_depth(os.path.join(depth_folder, tgt_name.replace(<span class="hljs-string">&#x27;.png&#x27;</span>, <span class="hljs-string">&#x27;&#x27;</span>)), depth)</td>
					</tr><tr class="" id="L46"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">46</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L47"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">47</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">clean_folder</span>(<span class="hljs-params">folder, img_exts=[<span class="hljs-string">&#x27;.png&#x27;</span>, <span class="hljs-string">&#x27;.jpg&#x27;</span>, <span class="hljs-string">&#x27;.npy&#x27;</span>]</span>):</span></td>
					</tr><tr class="" id="L48"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">48</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L49"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">49</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-keyword">for</span> img_ext <span class="hljs-keyword">in</span> img_exts:</td>
					</tr><tr class="" id="L50"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">50</td>
						<td class="px-3 overflow-visible whitespace-pre">        paths_to_check = os.path.join(folder, <span class="hljs-string">f&#x27;*<span class="hljs-subst">{img_ext}</span>&#x27;</span>)</td>
					</tr><tr class="" id="L51"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">51</td>
						<td class="px-3 overflow-visible whitespace-pre">        <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(glob.glob(paths_to_check)) == <span class="hljs-number">0</span>:</td>
					</tr><tr class="" id="L52"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">52</td>
						<td class="px-3 overflow-visible whitespace-pre">            <span class="hljs-keyword">continue</span></td>
					</tr><tr class="" id="L53"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">53</td>
						<td class="px-3 overflow-visible whitespace-pre">        print(paths_to_check)</td>
					</tr><tr class="" id="L54"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">54</td>
						<td class="px-3 overflow-visible whitespace-pre">        os.system(<span class="hljs-string">f&#x27;rm <span class="hljs-subst">{paths_to_check}</span>&#x27;</span>)</td>
					</tr><tr class="" id="L55"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">55</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr><tr class="" id="L56"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">56</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">resize_depth</span>(<span class="hljs-params">depth, width, height</span>):</span></td>
					</tr><tr class="" id="L57"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">57</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-string">&quot;&quot;&quot;Resize numpy (or image read by imageio) depth map</span></td>
					</tr><tr class="" id="L58"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">58</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-string"></span></td>
					</tr><tr class="" id="L59"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">59</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-string">    Args:</span></td>
					</tr><tr class="" id="L60"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">60</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-string">        depth (numpy): depth</span></td>
					</tr><tr class="" id="L61"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">61</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-string">        width (int): image width</span></td>
					</tr><tr class="" id="L62"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">62</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-string">        height (int): image height</span></td>
					</tr><tr class="" id="L63"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">63</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-string"></span></td>
					</tr><tr class="" id="L64"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">64</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-string">    Returns:</span></td>
					</tr><tr class="" id="L65"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">65</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-string">        array: processed depth</span></td>
					</tr><tr class="" id="L66"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">66</td>
						<td class="px-3 overflow-visible whitespace-pre"><span class="hljs-string">    &quot;&quot;&quot;</span></td>
					</tr><tr class="" id="L67"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">67</td>
						<td class="px-3 overflow-visible whitespace-pre">    depth = cv2.blur(depth, (<span class="hljs-number">3</span>, <span class="hljs-number">3</span>))</td>
					</tr><tr class="" id="L68"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">68</td>
						<td class="px-3 overflow-visible whitespace-pre">    <span class="hljs-keyword">return</span> cv2.resize(depth, (width, height), interpolation=cv2.INTER_AREA)</td>
					</tr><tr class="" id="L69"><td class="text-right select-none pl-5 pr-3 cursor-pointer text-gray-300 hover:text-black">69</td>
						<td class="px-3 overflow-visible whitespace-pre">
</td>
					</tr></tbody></table></div>
	</div></div></div></div></section></div></main>
	</div>

		<script>
			import("/front/build/module/index.f418ef775.js");
			window.supportsDynamicImport = true;
		</script>
		<script>
			if (!window.supportsDynamicImport) {
				const systemJsLoaderTag = document.createElement("script");
				systemJsLoaderTag.src =
					"https://unpkg.com/systemjs@2.0.0/dist/s.min.js";
				systemJsLoaderTag.addEventListener("load", function () {
					System.import("./front/build/nomodule/index.f418ef775.js");
				});
				document.head.appendChild(systemJsLoaderTag);
			}
		</script>

		<script type="text/javascript">
			/// LinkedIn (part 1)
			_linkedin_partner_id = "3734489";
			window._linkedin_data_partner_ids =
				window._linkedin_data_partner_ids || [];
			window._linkedin_data_partner_ids.push(_linkedin_partner_id);
		</script>

		<script>
			if (
				!(
					["localhost", "huggingface.test"].includes(
						window.location.hostname
					) || window.location.hostname.includes("ngrok.io")
				)
			) {
				(function (i, s, o, g, r, a, m) {
					i["GoogleAnalyticsObject"] = r;
					(i[r] =
						i[r] ||
						function () {
							(i[r].q = i[r].q || []).push(arguments);
						}),
						(i[r].l = 1 * new Date());
					(a = s.createElement(o)), (m = s.getElementsByTagName(o)[0]);
					a.async = 1;
					a.src = g;
					m.parentNode.insertBefore(a, m);
				})(
					window,
					document,
					"script",
					"https://www.google-analytics.com/analytics.js",
					"ganalytics"
				);
				ganalytics("create", "UA-83738774-2", "auto");
				ganalytics("send", "pageview");

				/// LinkedIn (part 2)
				(function (l) {
					if (!l) {
						window.lintrk = function (a, b) {
							window.lintrk.q.push([a, b]);
						};
						window.lintrk.q = [];
					}
					var s = document.getElementsByTagName("script")[0];
					var b = document.createElement("script");
					b.type = "text/javascript";
					b.async = true;
					b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
					s.parentNode.insertBefore(b, s);
				})(window.lintrk);
			}
		</script>

		<noscript>
			<!-- LinkedIn (part 3) -->
			<img
				height="1"
				width="1"
				style="display: none"
				alt=""
				src="https://px.ads.linkedin.com/collect/?pid=3734489&fmt=gif"
			/>
		</noscript>
	</body>
</html>
