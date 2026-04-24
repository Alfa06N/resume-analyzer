<script setup lang="ts">
import { motion } from "motion-v";

const currentYear = new Date().getFullYear();

const socialLinks = [
  { title: "GitHub", url: "https://github.com/Alfa06N/resume-analyzer" },
  {
    title: "LinkedIn",
    url: "https://www.linkedin.com/in/nicol%C3%A1s-alfaro-guzm%C3%A1n-7a9465270/",
  },
  {
    title: "Portfolio",
    url: "https://portfolio-phi-khaki-segxmki8ey.vercel.app/#about",
  },
];
</script>

<template>
  <footer
    class="relative mx-auto flex w-full flex-col items-center justify-center rounded-t-[2rem] border-t px-6 md:rounded-t-[3rem] md:px-8 bg-[radial-gradient(35%_128px_at_50%_0%,rgba(255,255,255,0.05),transparent)] dark:bg-[radial-gradient(35%_128px_at_50%_0%,rgba(255,255,255,0.1),transparent)]"
  >
    <div
      class="absolute top-0 right-1/2 left-1/2 h-px w-1/3 -translate-x-1/2 -translate-y-1/2 rounded-full bg-primary/40 blur-sm"
    ></div>

    <div class="grid w-full gap-8 py-8 md:grid-cols-2 lg:gap-12">
      <motion.div
        :initial="{ filter: 'blur(4px)', y: 10, opacity: 0 }"
        :whileInView="{ filter: 'blur(0px)', y: 0, opacity: 1 }"
        :transition="{ duration: 0.8 }"
        :inViewOptions="{ once: true }"
        class="space-y-3"
      >
        <h2 class="text-lg font-bold tracking-tight text-foreground">
          Portfolio Resume AI
        </h2>
        <p class="text-muted-foreground text-sm max-w-xs">
          Built with precision to help engineers bypass modern ATS systems.
        </p>
      </motion.div>

      <motion.div
        :initial="{ filter: 'blur(4px)', y: 10, opacity: 0 }"
        :whileInView="{ filter: 'blur(0px)', y: 0, opacity: 1 }"
        :transition="{ duration: 0.8, delay: 0.2 }"
        :inViewOptions="{ once: true }"
        class="flex flex-col md:items-end gap-4"
      >
        <h3
          class="text-xs uppercase tracking-widest text-muted-foreground font-semibold"
        >
          Connect
        </h3>
        <ul class="flex flex-wrap gap-6 text-muted-foreground text-sm">
          <li v-for="link in socialLinks" :key="link.title">
            <a
              :href="link.url"
              target="_blank"
              class="inline-flex items-center gap-2 duration-200 hover:text-primary transition-colors"
            >
              {{ link.title }}
            </a>
          </li>
        </ul>
      </motion.div>
    </div>

    <div
      class="h-px w-full bg-gradient-to-r from-transparent via-border to-transparent"
    ></div>

    <div class="flex w-full items-center justify-center py-6">
      <p class="text-muted-foreground text-xs">
        &copy; {{ currentYear }} Nicolás Alfaro. All rights reserved.
      </p>
    </div>
  </footer>
</template>
