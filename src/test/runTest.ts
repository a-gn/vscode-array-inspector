/**
 * Originally written by Claude (Sonnet 4.5) on 2025/11/14
 */

import * as path from 'path';
import { runTests } from '@vscode/test-electron';

async function main() {
    try {
        const extensionDevelopmentPath = path.resolve(__dirname, '../../');
        const extensionTestsPath = path.resolve(__dirname, './suite/index');
        const testWorkspace = path.resolve(__dirname, '../../');

        await runTests({
            extensionDevelopmentPath,
            extensionTestsPath,
            // Open the extension root as workspace so tests can access test-examples/
            launchArgs: [testWorkspace, '--disable-extensions']
        });
    } catch (err) {
        console.error('Failed to run tests:', err);
        process.exit(1);
    }
}

main();
