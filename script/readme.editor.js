const axios = require('axios');
const fs = require('fs');
const path = require('path');

async function updateReadme() {
    try {
        // README.md 파일의 경로 설정 및 내용 읽기
        const readmePath = path.join(__dirname, '..', 'README.md');
        const readmeContent = fs.readFileSync(readmePath, 'utf8');
        const readmeLines = readmeContent.split('\n');
        
        // 테이블 헤더의 위치를 찾음 (|------|)
        const headerIndex = readmeLines.findIndex(line => line.includes('|------|'));
        if (headerIndex === -1) {
            console.error('README.md에서 테이블 헤더를 찾을 수 없습니다.');
            return;
        }

        // solutions 폴더에 있는 모든 문제 파일(.cpp)을 읽어옴
        const solutionsPath = path.join(__dirname, '..', 'solutions');
        const files = fs.readdirSync(solutionsPath);
        const allProblemIds = files
            .filter(file => file.endsWith('.cpp'))
            .map(file => file.replace('.cpp', ''));

        if (allProblemIds.length === 0) {
            console.log('solutions 폴더에 풀이 파일이 없습니다.');
            return;
        }

        console.log(`총 ${allProblemIds.length}개의 문제를 업데이트합니다...`);

        const newTableRows = [];

        // 모든 문제 ID에 대해 API를 호출하여 테이블 행을 새로 생성
        for (const problemId of allProblemIds) {
            try {
                const solvedacResponse = await axios.get(`https://solved.ac/api/v3/problem/show?problemId=${problemId}`);
                const problem = solvedacResponse.data;
                
                // 새로운 테이블 행 생성 (해설 링크 포함)
                const newRow = `| ${problemId} | <img src="https://static.solved.ac/tier_small/${problem.level}.svg" width="20" height="20"> [${problem.titleKo}](https://www.acmicpc.net/problem/${problemId}) | [풀이](./solutions/${problemId}.py) | [해설](https://whqtker.github.io/posts/백준-${problemId}/) |`;
                newTableRows.push(newRow);
                console.log(`문제 ${problemId} 처리 완료`);
            } catch (error) {
                console.error(`Error fetching problem ${problemId}:`, error.message);
            }
        }
        
        // 문제 번호 오름차순으로 정렬
        const sortedRows = newTableRows.sort((a, b) => {
            const numA = parseInt(a.split('|')[1].trim());
            const numB = parseInt(b.split('|')[1].trim());
            return numA - numB;
        });
        
        // README.md 파일의 내용을 새로 구성
        // 테이블 이전 내용 + 테이블 헤더 + 새로 생성 및 정렬된 모든 행
        const newContent = [
            ...readmeLines.slice(0, headerIndex + 1), // 테이블 헤더까지의 내용 유지
            ...sortedRows
        ].join('\n');
        
        // README.md 파일에 새로운 내용 덮어쓰기
        fs.writeFileSync(readmePath, newContent);
        console.log('README.md 파일이 성공적으로 업데이트되었습니다.');

    } catch (error) {
        console.error('전체 작업 중 오류 발생:', error);
    }
}

updateReadme();