import axios from "axios";

const API_ENDPOINT = "http://localhost:8000";

enum QueryRole {
  USER = "user",
  SYSTEM = "system",
  FUNCTION = "function",
  ASSISTANT = "assistant",
}

interface Prompt {
  role: QueryRole;
  content: string;
}

interface Conversation {
  _id: string;
  name: string;
  params: object;
  tokens: number;
}
interface AllConversationsResponse {
  data: Conversation[];
}

interface ConversationFull extends Conversation {
  messages: Prompt[];
}

export const getAllConversations =
  async (): Promise<AllConversationsResponse> => {
    const response = await axios.get(`${API_ENDPOINT}/conversations`);
    return response.data as AllConversationsResponse;
  };

export const getFullConversation = async (
  conversationId: string
): Promise<ConversationFull> =>
  axios.get(`${API_ENDPOINT}/conversations/${conversationId}`);
