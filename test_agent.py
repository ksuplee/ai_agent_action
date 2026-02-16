from agent import get_agent_response

def test_prompt_quality():
    print("[CI] Prompt Evaluation 시작...")
    sample_response = get_agent_response("하늘은 왜 파란색이야?")

    if "[CONFIRMED]" in sample_response:
        print("품질 검증 통과: 형식을 준수함.")
        return True
    else:
        print("품질 검증 실패: 형식이 어긋남.")
        return False
