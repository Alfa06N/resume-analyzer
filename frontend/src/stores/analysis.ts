import { acceptHMRUpdate, defineStore } from "pinia";
import { ref } from "vue";
import apiClient from "@/api/client";
import { parseError } from "@/utils/errorHandler";
import { toast } from "vue-sonner";

interface AnalysisResult {
  score: number;
  keyword_gaps: string[];
  suggestions: string[];
  match_summary: string;
}

export const useAnalysisStore = defineStore("analysis", () => {
  const result = ref<AnalysisResult | null>(null);
  const loading = ref(false);
  const error = ref<string | null>(null);

  function reset() {
    result.value = null;
    loading.value = false;
    error.value = null;
  }

  async function analyzeResume(file: File, jobDescription: string) {
    loading.value = true;
    error.value = null;

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    try {
      const response = await apiClient.post(`/analyze`, formData);
      result.value = response.data;
    } catch (err: any) {
      const parsed = parseError(err);
      toast.error("Process Failed", {
        description: parsed.message,
        duration: 4000,
      });
    } finally {
      loading.value = false;
    }
  }

  return { result, loading, error, analyzeResume, reset };
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useAnalysisStore, import.meta.hot));
}
