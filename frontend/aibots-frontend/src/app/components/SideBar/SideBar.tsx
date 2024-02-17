import { getAllConversations } from "@/restHelpers/conversationHelper";
import { Button } from "@mantine/core";
import { useEffect } from "react";
import { useQuery } from "react-query";

const SideBar = () => {
  const { isLoading, error, data } = useQuery({
    queryKey: ["convoAll"],
    queryFn: getAllConversations,
  });

  return (
    <div className="w-1/6 h-full flex flex-col gap-2 bg-gray-100">
      <Button variant="outline" fullWidth>
        Add Conversation
      </Button>
      <>
        {data?.data.map((item) => {
          return (
            <p key={item._id} className="text-black">
              {item.name}
            </p>
          );
        })}
      </>
    </div>
  );
};

export default SideBar;
