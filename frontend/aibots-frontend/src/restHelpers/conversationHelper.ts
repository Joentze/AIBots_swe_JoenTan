import axios from "axios";

const API_ENDPOINT = "http://localhost:8000";

export enum QueryRole {
  USER = "user",
  SYSTEM = "system",
  FUNCTION = "function",
  ASSISTANT = "assistant",
}

export interface Prompt {
  role: QueryRole;
  content: string;
}

export interface Conversation {
  _id: string;
  name: string;
  params: object;
  tokens: number;
}
export interface AllConversationsResponse {
  data: Conversation[];
}

export interface ConversationFull extends Conversation {
  messages: Prompt[];
}

export const getAllConversations =
  async (): Promise<AllConversationsResponse> => {
    try {
      const response = await axios.get(`${API_ENDPOINT}/conversations`);
      return response.data as AllConversationsResponse;
    } catch (e) {
      throw Error(e as string);
    }
  };

export const getFullConversation = async (
  conversationId: string
): Promise<ConversationFull> => {
  try {
    const response = await axios.get(
      `${API_ENDPOINT}/conversations/${conversationId}`
    );
    return response.data as ConversationFull;
  } catch (e) {
    throw Error(e as string);
  }
};