export interface AppError {
  message: string;
  type: "validation" | "auth" | "server" | "network";
  raw?: any;
}

export const parseError = (err: any): AppError => {
  if (!err.response) {
    return {
      message:
        "We couldn't connect to the server. Please check your internet connection.",
      type: "network",
      raw: err,
    };
  }

  const status = err.response.status;
  const data = err.response.data;

  if (status >= 500) {
    const isOverloaded =
      status === 503 || data?.detail?.includes("high demand");
    const isExceeded = data?.detail?.toLowerCase().includes("exceeded");
    return {
      message: isOverloaded
        ? "The server is currently overloaded. Please try again later."
        : isExceeded
          ? "You have exceeded the rate limit. Please wait a moment and try again."
          : "An unexpected error occurred on the server. Please try again later.",
      type: "server",
      raw: data.detail || data.message || err.message,
    };
  }

  if (status === 422) {
    return {
      message: "There were validation errors with your input.",
      type: "validation",
      raw: data.detail || data.message || err.message,
    };
  }

  if (status === 429) {
    return {
      message:
        "We're receiving a lot of requests right now. Please wait a moment and try again.",
      type: "server",
      raw: data.detail || data.message || err.message,
    };
  }

  return {
    message: "An unexpected error occurred. Please try again.",
    type: "server",
    raw: data.detail || data.message || err.message,
  };
};
