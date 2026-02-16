# test_agent.py

from agent import get_agent_response

def test_prompt_quality():
    print("[CI] Prompt Evaluation 시작...")
    sample_response = get_agent_response("하늘은 왜 파란색이야?")

    # 리스트/딕셔너리 구조에서 text만 추출
    if isinstance(sample_response, list) and sample_response and isinstance(sample_response[0], dict):
        text = sample_response[0].get("text", "")
    else:
        text = str(sample_response)

    if "[CONFIRMED]" in text:
        print("품질 검증 통과: 형식을 준수함.")
        return True
    else:
        print("품질 검증 실패: 형식이 어긋남.")
        return False
    
# if __name__ == "__main__":
#    ok = test_prompt_quality()
#    raise SystemExit(0 if ok else 1)
