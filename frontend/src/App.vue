<script setup lang="ts">
import { storeToRefs } from "pinia";
import AnalyzerCard from "./components/AnalyzerCard.vue";
import ResultsDisplay from "./components/ResultsDisplay.vue";
import { useAnalysisStore } from "./stores/analysis";
import Footer from "./components/Footer.vue";
import AnalysisPlaceholder from "./components/AnalysisPlaceholder.vue";
import { AnimatePresence } from "motion-v";
import "vue-sonner/style.css";
import { Toaster } from "./components/ui/sonner";

const store = useAnalysisStore();
const { result } = storeToRefs(store);
</script>

<template>
  <div class="dark flex flex-col w-full min-h-screen bg-background">
    <main class="flex-1 h-full w-full bg-background py-12 px-4">
      <div class="max-w-5xl mx-auto">
        <div class="text-center mb-10">
          <h1 class="text-4xl font-extrabold tracking-tight text-foreground">
            Portfolio Resume AI
          </h1>
          <p class="text-muted-foreground mt-2">
            Optimize your application for modern ATS systems.
          </p>
        </div>

        <AnalyzerCard />

        <AnimatePresence mode="popLayout">
          <AnalysisPlaceholder v-if="!result" key="placeholder" />

          <ResultsDisplay v-if="result" key="display" />
        </AnimatePresence>
      </div>
    </main>
    <Footer />
    <Toaster theme="dark" richColors position="bottom-right" />
  </div>
</template>
