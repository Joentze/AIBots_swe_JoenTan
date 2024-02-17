import { useDisclosure } from "@mantine/hooks";
import { Modal, Button, Input, JsonInput, ActionIcon } from "@mantine/core";
import { IoAdd, IoCog } from "react-icons/io5";
import { useState } from "react";
import { useConversation } from "@/app/customHooks/conversationHooks";
import { validateCreateConversation } from "@/validators/validateCreateConversation";
import { createConversation } from "@/restHelpers/conversationHelper";

interface IEditConvoPopup {
  name: string;
  params: string;
}

const EditConvoPopup: React.FC<IEditConvoPopup> = ({ name, params }) => {
  const { conversationId, setConversationId } = useConversation();
  const [loading, setLoading] = useState<boolean>(false);
  const [opened, { open, close }] = useDisclosure(false);
  const [conversationName, setConversationName] = useState<string>(name);
  const [jsonValue, setJsonValue] = useState(JSON.stringify(params));

  const createConvo = async () => {
    try {
      validateCreateConversation(conversationName, jsonValue);
      setLoading(true);
      const { id } = await createConversation({
        name: conversationName,
        params: JSON.parse(jsonValue),
        tokens: 0,
      });
      setLoading(false);
      setConversationId(id);
    } catch (e) {
      alert(e);
    }
  };
  return (
    <>
      <Modal
        opened={opened}
        onClose={close}
        title="Edit Conversation Settings 📝"
      >
        <Modal.Body>
          <Input.Wrapper
            label="Rename Conversation"
            description="Edit your conversation name to suit your task better!"
          >
            <Input
              defaultValue={name}
              value={conversationName}
              placeholder="Example: an Exploration into Large Language Models"
              onChange={(event) => setConversationName(event.target.value)}
            />
          </Input.Wrapper>
          <br></br>

          <Input.Wrapper
            label="Conversation Parameters"
            description="Set OpenAI chat parameters"
          >
            <JsonInput
              defaultValue={params}
              value={jsonValue}
              onChange={setJsonValue}
              mt={8}
            />
          </Input.Wrapper>
          <br></br>
          <Button
            loading={loading}
            loaderProps={{ type: "dots" }}
            fullWidth
            onClick={async () => {
              await createConvo();
              close();
            }}
          >
            Confirm
          </Button>
        </Modal.Body>
      </Modal>

      <ActionIcon size={"lg"} variant="light" onClick={open}>
        <IoCog size={"md"} />
      </ActionIcon>
    </>
  );
};

export default EditConvoPopup;
